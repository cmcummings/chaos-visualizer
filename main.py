"""

Mathematical Chaos Visualizer
Inspired by CodeParade's Chaos-Equations (https://github.com/HackerPoet/Chaos-Equations)

Requirements:
- pygame

Usage:
- Windows: py -3 main.py
- Linux/Mac: python3 main.py

"""
from config import *
from algorithm import Algorithm
from display import Visualizer
from utils import current_time_millis
import pygame, sys, time


class Main:

    def __init__(self):
        # Initialization
        pygame.init()
        self.visualizer = Visualizer()
        self.algorithm = Algorithm()

        self.speed_scl = 1

        self.released = {}

        self.last_tick = current_time_millis()
        self.current_tick = current_time_millis()

        print("------------------------")
        print("        Controls:       ")
        print("[WASD]: Move the graph.")
        print("[UP ARROW]: Zoom in.")
        print("[DOWN ARROW]: Zoom out.")
        print("[LEFT ARROW]: Slow down.")
        print("[RIGHT ARROW]: Speed up.")
        print("------------------------")

        # Main loop
        while True:
            if self.current_tick - self.last_tick > 1000/SPEED:
                self.tick()
                self.last_tick = current_time_millis()
            else:
                self.current_tick = current_time_millis()
    
    def tick(self):
        # Handle program quit event
        for event in pygame.event.get():
            if event.type == pygame.QUIT: sys.exit()

        # Key handling
        pressed = pygame.key.get_pressed()
        # Increase speed
        if pressed[pygame.K_RIGHT] != 0:
            if pygame.K_RIGHT in self.released:
                if self.released[pygame.K_RIGHT]:
                    self.speed_scl = min(4, self.speed_scl + 1)
                    self.algorithm.time_increment = SPEEDS[self.speed_scl]
                    self.released[pygame.K_RIGHT] = False
        elif pressed[pygame.K_RIGHT] == 0:
            self.released[pygame.K_RIGHT] = True
        
        # Decrease speed
        if pressed[pygame.K_LEFT] != 0:
            if pygame.K_LEFT in self.released:
                if self.released[pygame.K_LEFT]:
                    self.speed_scl = max(-4, self.speed_scl - 1)
                    self.algorithm.time_increment = SPEEDS[self.speed_scl]
                    self.released[pygame.K_LEFT] = False
        elif pressed[pygame.K_LEFT] == 0:
            self.released[pygame.K_LEFT] = True

        # Reset
        if pressed[pygame.K_r] != 0:
            self.algorithm.reset()

        # Pause
        if pressed[pygame.K_SPACE] != 0:
            self.speed_scl = 0
            self.algorithm.time_increment = SPEEDS[self.speed_scl]
            
        
        # Advance the algorithm
        points = self.algorithm.advance()
        self.visualizer.update_points(points)

        # Visualizer tick
        self.visualizer.tick()
        self.visualizer.draw_t(self.algorithm.t)
        self.visualizer.draw_speed(self.speed_scl)

        pygame.display.flip() # Buffer
        


if __name__ == "__main__":
    Main()