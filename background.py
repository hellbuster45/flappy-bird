import pygame as po
import gamedata as gd
import random as r

class Background:
    def __init__(this, screen):
        
        bg_back = po.image.load(r'assets\background\back-trees.png').convert_alpha()
        bg_lights = po.image.load(r'assets\background\lights.png').convert_alpha()
        bg_middle = po.image.load(r'assets\background\middle-trees.png').convert_alpha()
        bg_front = po.image.load(r'assets\background\front-trees.png').convert_alpha()

        scale_factor = gd.height / (bg_back.get_height())
        this.full_height = bg_back.get_height() * scale_factor
        this.full_width = bg_back.get_width() * scale_factor

        this.bg_back = po.transform.scale(bg_back, (this.full_width, this.full_height))
        this.bg_lights = po.transform.scale(bg_lights, (this.full_width, this.full_height))
        this.bg_middle = po.transform.scale(bg_middle, (this.full_width, this.full_height))
        this.bg_front = po.transform.scale(bg_front, (this.full_width, this.full_height))

        this.back_rect = this.bg_back.get_rect()
        this.light_rect = this.bg_back.get_rect()
        this.middle_rect = this.bg_back.get_rect()
        this.front_rect = this.bg_back.get_rect()
        
        this.screen = screen

    def draw(this, scroll_speed):
        this.back_rect.x += scroll_speed * 0.3
        this.light_rect.x += scroll_speed * 0.5
        this.middle_rect.x += scroll_speed * 0.7
        this.front_rect.x += scroll_speed * 0.9

        if this.back_rect.right <= 0:
            this.back_rect.x = 0
        if this.light_rect.right <= 0:
            this.light_rect.x = 0
        if this.middle_rect.right <= 0:
            this.middle_rect.x = 0
        if this.front_rect.right <= 0:
            this.front_rect.x = 0
        
        this.screen.blit(this.bg_back, (this.back_rect.x, 0))
        this.screen.blit(this.bg_back, (this.full_width + this.back_rect.x, 0))
        this.screen.blit(this.bg_lights, (this.light_rect.x, 0))
        this.screen.blit(this.bg_lights, (this.full_width + this.light_rect.x, 0))
        this.screen.blit(this.bg_middle, (this.middle_rect.x, 0))
        this.screen.blit(this.bg_middle, (this.full_width + this.middle_rect.x, 0))
        this.screen.blit(this.bg_front, (this.front_rect.x, 0))
        this.screen.blit(this.bg_front, (this.full_width + this.front_rect.x, 0))