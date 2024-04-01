import pygame as po
po.mixer.init()
width = 800
height = 600
gravity = 0.4
pipe_freq = 1200
pipe_group = po.sprite.Group()
jumpfx = po.mixer.Sound(r'assets\sfx\jump.wav')
jumpfx.set_volume(0.2)
deathfx = po.mixer.Sound(r'assets\sfx\hitHurt.wav')
deathfx.set_volume(0.2)
scorefx = po.mixer.Sound(r'assets\sfx\score.wav')
scorefx.set_volume(0.1)