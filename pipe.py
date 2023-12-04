import pygame as po

class Pipe(po.sprite.Sprite):
    def __init__(this, x, y, location):
        super().__init__()
        this.image = po.image.load(r'assets\pipe - Copy.png').convert_alpha()
        this.rect = this.image.get_rect()
        this.rect.topleft = (x, y)
        pipe_gap = 129
        if location == -1:
            this.image = po.transform.flip(this.image, False, True)
            this.rect.bottomleft = (x, y - pipe_gap // 2)
        if location == 1:
            this.rect.topleft = (x, y + pipe_gap // 2)
    
    def update(this, scroll_speed):
        this.rect.x += scroll_speed