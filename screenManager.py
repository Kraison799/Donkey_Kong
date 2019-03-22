"""
Instituto Tecnológico de Costa Rica (TEC)
Área Académica de Ingeniería en Computadores
Introducción y Taller de Programación
I Semestre, 2017

Víctor Ignacio Castrillo Muñoz
Carné: 2017110244

Proyecto #1: Donkey Kong
Screen Manager File

Python 3.7.2
Pygame 1.9.3
"""

import pygame, time
from Player import *
from Platform import *

# Game Screen
class GameScreen():
    def __init__(self, frame):
        self.frame = frame
        self.player = Player(475, 100)
        self.platforms = [Block(0, 625, 1000, 25), Block(100, 550, 200, 25), Block(600, 400, 200, 25)]

    def respawn(self):
        self.player = Player(475, 100)

    def __update__(self, event):
        if event.type == pygame.KEYUP:
            if event.key == pygame.K_LEFT or event.key == pygame.K_a:
                self.player.action = 'standing'
                self.player.state = 'left'
            if event.key == pygame.K_RIGHT or event.key == pygame.K_d:
                self.player.action = 'standing'
                self.player.state = 'right'
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_LEFT or event.key == pygame.K_a:
                self.player.action = 'walking'
                self.player.state = 'left'
            if event.key == pygame.K_RIGHT or event.key == pygame.K_d:
                self.player.action = 'walking'
                self.player.state = 'right'
            self.player.sprite_index = -1

            if event.key == pygame.K_SPACE:
                self.respawn()

    def __draw__(self):
        playerFalling = True
        for platform in self.platforms:
            if self.player.rect.colliderect(platform.rect):
                playerFalling = False
        if playerFalling:
            self.player.rect.top += 7

        self.frame.fill((0, 0, 255))
        self.player.__update__()
        self.player.__draw__(self.frame)
        for platform in self.platforms:
            platform.__draw__(self.frame)
        time.sleep(0.09)
