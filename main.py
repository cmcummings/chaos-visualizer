"""

Mathematical Chaos Visualizer
Inspired by CodeParade's Chaos-Equations (https://github.com/HackerPoet/Chaos-Equations)

Requirements:
- pygame

Usage:
- Windows: py -3 main.py
- Linux/Mac: python3 main.py

"""

from algorithm import *
from display import *
import pygame, sys


# Initialization
pygame.init()
visualizer = Visualizer()
algorithm = Algorithm()

# Main loop
while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT: sys.exit()

    visualizer.tick()

    pygame.display.flip()