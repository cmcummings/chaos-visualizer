# display.py
from config import *
import pygame

class Visualizer:
    """Handles visualization of the equation."""

    def __init__(self):
        # Initialize screen
        self.screen = pygame.display.set_mode(WINDOW_SIZE)
        self.points = [] # List of Points

    def add_point(self, x, y):
        """Creates a new Point object and adds its to the points array."""
        self.points.append(Point(x, y))

    def tick(self):
        for point in self.points:
            point.tick()
        self.logic()
        self.draw()

    def logic(self):
        for point in self.points:
            # Remove points from the array that are not being seen
            if point.transparency <= 0: 
                self.points.remove(point)

    def draw(self):
        pass


class Point:
    """A visualized point."""

    fade_rate = 0.1 # How much the transparency of a point is reduced per tick

    def __init__(self, x, y):
        self.transparency = 1
        self.coords = self.x, self.y = x, y

    def tick(self):
        self.logic()
        self.draw()

    def logic(self):
        self.transparency -= self.fade_rate # Fade the pixel

    def draw(self):
        pass