import pygame as po
import gamedata as gd

class Player(po.sprite.Sprite):
    def __init__(this, x, y):
        super().__init__()
        this.sprites = []
        temp = None
        scale_factor = 2
        for i in range(4):
            temp = po.image.load(f'assets\\bird\\bird{i + 1}.png').convert_alpha()
            temp = po.transform.scale(temp, (temp.get_width() * scale_factor, temp.get_height() * scale_factor))
            this.sprites.append(temp)
        this.image = this.sprites[0]
        this.frame_index = 0
        this.update_time = po.time.get_ticks()
        this.rect = this.image.get_rect(topleft = (x, y))
        
        this.alive = True
        this.jump = False
        this.jump_counter = 0
        this.y_velocity = 0
        this.pressed = False
        
    def update_animation(this):
        COOLDOWN = 100
        this.image = po.transform.rotate(this.sprites[this.frame_index], this.y_velocity * -2)

        if po.time.get_ticks() - this.update_time > COOLDOWN:
            this.update_time = po.time.get_ticks()
            this.frame_index += 1
        
        if this.frame_index >= len(this.sprites):
            this.frame_index = 0
    
    def move(this):
        dy = 0
        if this.alive:    
            if this.jump and (this.pressed == False):
                this.y_velocity = -7
                gd.jumpfx.play()
                this.pressed = True
        else:
            this.image = po.transform.rotate(this.sprites[this.frame_index], -90)
            
        this.y_velocity += gd.gravity
        dy += this.y_velocity
        
        if this.rect.top + dy < 0:
            dy = 0
            
        if this.rect.bottom < gd.height:
            this.rect.y += dy
        else:
            this.alive = False
        if this.y_velocity > 50:
            this.y_velocity = 0
        