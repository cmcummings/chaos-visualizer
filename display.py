# display.py
from config import *
from utils import random_color, random_grayscale, round_to_place, color_sequence
import pygame

class Visualizer:
    """Handles visualization of the equation."""


    def __init__(self):

        # Graph variables
        self.x_offset, self.y_offset = WIDTH/2, HEIGHT/2
        self.x_zoom, self.y_zoom = 400, 400
        self.colors = color_sequence(ITERATIONS)

        # Initialize screen
        self.screen = pygame.display.set_mode(WINDOW_SIZE)
        pygame.display.set_caption("Chaos Visualizer")
        self.font = pygame.font.Font(None, 20)

        # Initialize points list
        self.points = [] 
        self.trails = []
        self.prev_points = []

    def update_points(self, points):
        """Creates a new Point object for each point, calculates where it should be on the screen, 
           and adds it to the points array."""
        # Reset points array
        self.prev_points = self.points
        self.points = []

        # Move the current points to previous points
        for i, point in enumerate(points):
            x = point[0] * self.x_zoom + self.x_offset
            y = point[1] * self.y_zoom + self.y_offset
            obj = Point(int(x), int(y), self.colors[i])
            self.points.append(obj)


    def tick(self):
        self.logic()
        self.clear()
        for point in self.points:
            point.tick(self.screen)

    def logic(self):
        # Key handling
        pressed = pygame.key.get_pressed()
        if pressed[pygame.K_UP] != 0:
            self.zoom_in()
        if pressed[pygame.K_DOWN] != 0:
            self.zoom_out()
        if pressed[pygame.K_w] != 0:
            self.move(0, MOVE_SPEED)
        if pressed[pygame.K_s] != 0:    
            self.move(0, -MOVE_SPEED)
        if pressed[pygame.K_a] != 0:    
            self.move(MOVE_SPEED, 0)
        if pressed[pygame.K_d] != 0:    
            self.move(-MOVE_SPEED, 0)

    def clear(self):
        self.screen.fill(pygame.Color(0, 0, 0)) # Clear the screen
    
    def draw_t(self, t):
        """Draws the time counter."""
        # Draw the UI
        text = self.font.render("t = " + str(round_to_place(t, 100000)), True, (255, 255, 255))
        self.screen.blit(text, (WIDTH-text.get_width()-10, text.get_height()))

    def draw_speed(self, speed_scl):
        """Draws the speed level."""
        text = "||"
        if speed_scl > 0:
            text =  ">" * speed_scl 
        elif speed_scl < 0:
            text = "<" * abs(speed_scl)

        text = self.font.render(text, True, (255, 255, 255))
        self.screen.blit(text, (WIDTH-text.get_width()-10, text.get_height()+20))

    def zoom_in(self):
        self.x_zoom = min(5000, self.x_zoom + ZOOM_RATE)
        self.y_zoom = min(5000, self.y_zoom + ZOOM_RATE)

    def zoom_out(self):
        self.x_zoom = max(100, self.x_zoom - ZOOM_RATE)
        self.y_zoom = max(100, self.y_zoom - ZOOM_RATE)

    def move(self, left, up):
        """Moves the focus."""
        self.x_offset += left
        self.y_offset += up


class Point:
    """A visualized point."""

    fade_rate = 15 # How much the transparency of a point is reduced per tick

    def __init__(self, x, y, color=None):
        if color is None:
            self.color = random_grayscale()
        else:
            self.color = color
        self.pixel = pygame.Surface((1, 1))
        self.pixel.set_alpha(255)
        self.pixel.fill(self.color) 
        self.x, self.y = x, y

    def tick(self, screen):
        self.logic()
        self.draw(screen)

    def logic(self):
        pass

    def draw(self, screen):
        try:
            screen.blit(self.pixel, (self.x, self.y))
        except TypeError:
            print("Error drawing... resetting algorithm.")