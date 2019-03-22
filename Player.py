"""
Instituto Tecnológico de Costa Rica (TEC)
Área Académica de Ingeniería en Computadores
Introducción y Taller de Programación
I Semestre, 2017

Víctor Ignacio Castrillo Muñoz
Carné: 2017110244

Proyecto #1: Donkey Kong
Platforms File

Python 3.7.2
Pygame 1.9.3
"""

# Libraries
import pygame

# Settings
pygame.init()
transColor = pygame.Color(255, 0, 255)

# Player Class
class Player:
    def __init__(self, x, y):
        self.spriteSheet = pygame.image.load('rsc/PikachuSprite.png')

        # Standing sprite
        self.spriteSheet.set_clip(1, 1, 36, 38)
        self.standing = self.spriteSheet.subsurface(self.spriteSheet.get_clip()).convert()
        self.standing.set_colorkey(transColor)

        # Walking sprites
        self.spriteSheet.set_clip(1, 45, 52, 30)
        walking1 = self.spriteSheet.subsurface(self.spriteSheet.get_clip()).convert()
        walking1.set_colorkey(transColor)
        self.spriteSheet.set_clip(53, 45, 52, 30)
        walking2 = self.spriteSheet.subsurface(self.spriteSheet.get_clip()).convert()
        walking2.set_colorkey(transColor)
        self.spriteSheet.set_clip(105, 45, 52, 30)
        walking3 = self.spriteSheet.subsurface(self.spriteSheet.get_clip()).convert()
        walking3.set_colorkey(transColor)
        self.spriteSheet.set_clip(157, 45, 52, 30)
        walking4 = self.spriteSheet.subsurface(self.spriteSheet.get_clip()).convert()
        walking4.set_colorkey(transColor)
        self.walking = [walking1, walking2, walking3, walking4]

        # Climbing sprites

        # Settings
        self.sprite = self.standing
        self.sprite_index = 0
        self.rect = self.sprite.get_rect()
        self.rect.topleft = (x, y)
        self.action = 'standing'
        self.state = 'right'
        self.jumpTime = 1.5
        self.tag = 'player'

    def __update__(self):
        if self.action == 'standing':
            if self.state == 'left':
                self.sprite = self.standing
                self.sprite = pygame.transform.flip(self.standing, True, False)
            elif self.state == 'right':
                self.sprite = self.standing
        elif self.action == 'walking':
            if self.state == 'left':
                self.rect.left -= 7
                self.sprite = self.__get_sprite__(self.walking)
                self.sprite = pygame.transform.flip(self.sprite, True, False)
            elif self.state == 'right':
                self.rect.right += 7
                self.sprite = self.__get_sprite__(self.walking)

    def __draw__(self, frame):
        pygame.draw.rect(frame, (255, 0, 0), self.rect)
        if self.action == 'standing':
            frame.blit(self.sprite, (self.rect.left, self.rect.top))
        elif self.action == 'walking':
            if self.state == 'left':
                frame.blit(self.sprite, (self.rect.left, self.rect.top + 10))
            elif self.state == 'right':
                frame.blit(self.sprite, (self.rect.left - 16, self.rect.top + 10))

    def __get_sprite__(self, sprites):
        self.sprite_index += 1
        if self.sprite_index >= (len(sprites)):
            self.sprite_index = 0
        return sprites[self.sprite_index]

# Closing pygame
pygame.quit()
