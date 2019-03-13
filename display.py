# display.py
from config import *
from utils import random_color
import pygame

class Visualizer:
    """Handles visualization of the equation."""

    colors = [random_color() for i in range(ITERATIONS)]

    def __init__(self, x_min, x_max):
        # Graph variables
        self.x_res, self.y_res = WIDTH, HEIGHT
        self.x_min, self.x_max = x_min, x_max
        self.y_min, self.y_max = 0, 0

        self.x_scl, self.y_scl = 1, 1 # Zoom

        # Initialize screen
        self.screen = pygame.display.set_mode(WINDOW_SIZE)

        # Initialize points list
        self.points = [] 
        self.prev_points = []

    def update_points(self, points):
        """Creates a new Point object for each point, calculates where it should be on the screen, 
           and adds it to the points array."""
        # screen_x, screen_y = self.calc_screen_pos(x, y)
        # Move the current points to previous points
        self.prev_points = self.points
        self.points = []
        
        for i, point in enumerate(points):
            x, y = point[0], point[1]
            self.points.append(Point(int(x*400+WIDTH/2), int(y*400+2*HEIGHT/3), self.colors[i]))

    def tick(self):
        self.logic()
        self.draw()
        for point in self.points:
            point.tick(self.screen)

    def logic(self):
        for point in self.points:
            # Remove points from the array that are not being seen
            if point.pixel.get_alpha() <= 0: 
                self.points.remove(point)

    def draw(self):
        self.screen.fill(pygame.Color(0, 0, 0)) # Clear the screen

        # Draw the trails
        for i in range(len(self.prev_points)):
            point = self.points[i]
            prev_point = self.prev_points[i]

            pygame.draw.line(self.screen, point.color, (point.x, point.y), (prev_point.x, prev_point.y))

    def calc_screen_pos(self, x, y):
        """Converts the coordinates of a point to coordinates on the screen."""
        pass

class Point:
    """A visualized point."""

    fade_rate = 15 # How much the transparency of a point is reduced per tick

    def __init__(self, x, y, color):
        self.color = color
        self.pixel = pygame.Surface((1, 1))
        self.pixel.set_alpha(255)
        self.pixel.fill(color)  
        self.x, self.y = x, y

    def tick(self, screen):
        self.logic()
        self.draw(screen)

    def logic(self):
        alpha = self.pixel.get_alpha()
        new_alpha = alpha - self.fade_rate
        if new_alpha >= 0:
            self.pixel.set_alpha(new_alpha) # Fade the pixel

    def draw(self, screen):
        screen.blit(self.pixel, (self.x, self.y))
