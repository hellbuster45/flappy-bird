import pygame as po
import gamedata as gd
import random as r
from background import Background
from player import Player
from pipe import Pipe

po.init()
po.mixer.init()
screen = po.display.set_mode((gd.width, gd.height))
po.display.set_caption('Flappy Bird')

def display_text(text, font, color, x, y):
    img = font.render(text, True, color)
    screen.blit(img, (x, y))

def reset_game():
    gd.pipe_group.empty()
    player = player = Player(100, 200)
    score = 0
    restart = False
    return player, score, restart

class Button:
    def __init__(this, x, y):
        this.image = po.image.load(r'assets\restart1.png')
        this.rect = this.image.get_rect()
        this.rect.center = (x, y)
        this.restart = False
    
    def draw(this):
        pos = po.mouse.get_pos()

        if this.rect.collidepoint(pos):
            if po.mouse.get_pressed()[0]:
                this.restart = True
        screen.blit(this.image, this.rect)
        return this.restart
        

def main():
    clock = po.time.Clock()
    last_time = po.time.get_ticks() - gd.pipe_freq
    po.mixer.music.load('assets\sfx\Blaster Master (NES) Music - Area 3 (320kbps).mp3')
    po.mixer.music.set_volume(0.3)
    po.mixer.music.play(-1, 0.0)
    bg = Background(screen)
    player = Player(100, 200)
    restart_button = Button(gd.width // 2, gd.height // 2)
    run = True
    score = 0
    scroll_speed = -4
    font = po.font.SysFont('Bauhaus 93', 60)
    menu_font = po.font.Font(r'assets\fonts\misty_style\Misty Style.ttf', 100)
    menu_font_medium = po.font.Font(r'assets\fonts\misty_style\Misty Style.ttf', 45)
    start_game = False
    game_over = False
    flying = False
    while run:
        clock.tick(75)
        screen.fill((50, 50, 50))
        
        if start_game == False:
            bg.draw(0)
            display_text('FLAPPY BIRD', menu_font, (20, 194, 194), 100, 30)
            screen.blit(player.image, player.rect)
            player.update_animation()
            display_text('Press SPACE or UP_ARROW to start !!', menu_font_medium, (255, 255, 128), 20, 400)
        else:
            bg.draw(scroll_speed)
            if player.alive == False:
                scroll_speed = 0
                flying = False
            
            screen.blit(player.image, player.rect)
            player.move()
            if player.alive:
                player.update_animation()
                scroll_speed = -4
                
                current_time = po.time.get_ticks()
                if current_time - last_time > gd.pipe_freq:
                    random_position = (r.randrange(-9, 9, 3) * 2) * 10
                    pipe1 = Pipe(gd.width, (gd.height // 2) + random_position, 1)
                    pipe2 = Pipe(gd.width, (gd.height // 2) + random_position, -1)
                    gd.pipe_group.add(pipe1, pipe2)
                    last_time = current_time
                    
                for pipe in gd.pipe_group:
                    if pipe.rect.colliderect(player.rect):
                        player.alive = False
                        gd.deathfx.play()
                    if pipe.rect.right < 0:
                        pipe.kill()
                    
                    if pipe.rect.left < player.rect.right < pipe.rect.right + 5:
                        if player.rect.right > pipe.rect.right:
                            score += 1
                            gd.scorefx.play()
                gd.pipe_group.draw(screen)
                gd.pipe_group.update(scroll_speed - 1)
            else:
                player.alive = False
                restart_button.draw()
                display_text('Click to restart', menu_font_medium, (255, 255, 0), 245, 350)
                display_text('OR', menu_font_medium, (255, 255, 0), 370, 400)
                display_text('Press F to restart !!', menu_font_medium, (255, 255, 0), 210, 450)
                if restart_button.draw():
                    player, score ,restart_button.restart = reset_game()
            display_text(str(score // 2), font, (0, 255, 0), gd.width // 2, 20)
        
        for event in po.event.get():
            if event.type == po.QUIT:
                run = False
            if event.type == po.KEYDOWN:
                if event.key in (po.K_SPACE, po.K_UP, po.K_z):
                    if start_game == False:
                        start_game = True
                    flying = True
                    player.jump = True
                if event.key == po.K_f:
                    if not player.alive:
                        restart_button.restart = True
                
            if event.type == po.KEYUP:
                if event.key in (po.K_SPACE, po.K_UP, po.K_z):
                    player.jump = False
                    player.pressed = False
        po.display.update()
    po.quit()
main()