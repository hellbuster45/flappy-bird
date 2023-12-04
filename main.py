import pygame as po
import gamedata as gd
import random as r
from background import Background
from player import Player
from pipe import Pipe

po.init()
screen = po.display.set_mode((gd.width, gd.height))
po.display.set_caption('Flappy Bird')

def display_score(score, font, color, x, y):
    img = font.render(score, True, color)
    screen.blit(img, (x, y))

def main():
    clock = po.time.Clock()
    last_time = po.time.get_ticks() - gd.pipe_freq
    
    bg = Background(screen)
    player = Player(100, gd.width // 2)
    
    run = True
    score = 0
    scroll_speed = -4
    font = po.font.SysFont('Bauhaus 93', 60)
    game_over = False
    flying = False
    while run:
        clock.tick(75)
        screen.fill((50, 50, 50))
        
        if player.alive == False:
            scroll_speed = 0
            flying = False
        
        bg.draw(scroll_speed)
        screen.blit(player.image, player.rect)
        
        if player.rect.bottom < gd.height and flying == True:
            player.update_animation()
            player.move()
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
                if pipe.rect.right < 0:
                    pipe.kill()
                
                if pipe.rect.left < player.rect.right < pipe.rect.right + 3:
                    if player.rect.right > pipe.rect.right:
                        score += 1
            gd.pipe_group.draw(screen)
            gd.pipe_group.update(scroll_speed)
                
        elif player.rect.bottom >= gd.height:
            player.alive = False
        display_score(str(score // 2), font, (0, 255, 0), gd.width // 2, 20)
        
        for event in po.event.get():
            if event.type == po.QUIT:
                run = False
            if event.type == po.KEYDOWN:
                if event.key in (po.K_SPACE, po.K_UP, po.K_z):
                    flying = True
                    player.jump = True
            
            if event.type == po.KEYUP:
                if event.key in (po.K_SPACE, po.K_UP, po.K_z):
                    player.jump = False
                    player.pressed = False
        po.display.update()
    po.quit()
main()