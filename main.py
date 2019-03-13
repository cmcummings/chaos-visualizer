"""

Mathematical Chaos Visualizer
Inspired by CodeParade's Chaos-Equations (https://github.com/HackerPoet/Chaos-Equations)

Requirements:
- pygame

Usage:
- Windows: py -3 main.py
- Linux/Mac: python3 main.py

"""
from config import SPEED
from algorithm import Algorithm
from display import Visualizer
from utils import current_time_millis
import pygame, sys, time


# Initialization
pygame.init()
visualizer = Visualizer(-2, 2)
algorithm = Algorithm(t=0.3)

def tick():
    # Handle program quit event
    for event in pygame.event.get():
        if event.type == pygame.QUIT: sys.exit()

    # Advance the algorithm
    points = algorithm.advance()
    visualizer.update_points(points)

    # Visualizer tick
    visualizer.tick()

    pygame.display.flip() # Buffer


# Main loop
last_tick = current_time_millis()
current_tick = current_time_millis()
while True:
    if current_tick - last_tick > 1000/SPEED:
        tick()
        last_tick = current_time_millis()
    else:
        current_tick = current_time_millis()
