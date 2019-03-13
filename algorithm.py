# algorithm.py
from config import *


# Example:
# x' = x^2 - xt + yt - x
# y' = -y^2 - t^2 - xy - xt - yt - y


class Algorithm:
    """Handles computation of the equation."""

    time_increment = TIME_INCREMENT

    def __init__(self, t=TIME_DEFAULT):
        self.t = t

    def advance(self):
        """Increments t by time_increment and recalculates.
           Returns an array of the new points."""
        self.t += self.time_increment
        return self.calculate()

    def calculate(self):
        """Recalculates the equation. 
           Returns an array of the new points."""
        points = [] # Where all the points will be stored

        # Initialize coordinates to t
        x, y = self.t, self.t

        # Calculate
        for i in range(ITERATIONS):
            # Calculate x' and y'
            try:
                x = x ** 2 - x * self.t + y * self.t - x
                y = -y ** 2 - self.t ** 2 - x * y - x * self.t - y * self.t - y
            except OverflowError:
                self.t = TIME_INCREMENT
                x, y = self.t, self.t

            # Save the point
            points.append((x, y))
        
        return points

    def reset(self):
        self.t = TIME_DEFAULT