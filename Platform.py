"""
Instituto Tecnológico de Costa Rica (TEC)
Área Académica de Ingeniería en Computadores
Introducción y Taller de Programación
I Semestre, 2017

Víctor Ignacio Castrillo Muñoz
Carné: 2017110244

Proyecto #1: Donkey Kong
Platform File

Python 3.7.2
Pygame 1.9.3
"""

# Libraries
import pygame

# Settings
pygame.init()
transColor = pygame.Color(255, 0, 255)

# Block Class
class Block:
    def __init__(self, x, y, width, height):
        # Settings
        self.rect = (x, y, width, height)
        self.tag = 'block'

    def __draw__(self, frame):
        pygame.draw.rect(frame, (0, 255, 0), self.rect)

# Closing pygame
pygame.quit()
