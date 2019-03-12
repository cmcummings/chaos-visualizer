# algorithm.py

# Example:
# x' = x^2 - xt + yt - x
# y' = -y^2 - t^2 - xy - xt - yt - y


class Algorithm:
    """Handles computation of the equation."""

    time_increment = 0.0001

    def __init__(self, x=0, y=0, time_start=0):
        self.t = time_start
        self.coords = self.x, self.y = x, y

    def advance(self):
        """Increments t by time_increment and recalculates.
           Returns the new (x, y) coordinates."""
        self.t += self.time_increment
        return self.calculate()

    def calculate(self):
        """Recalculates the equation. 
           Returns the new (x, y) coordinates."""
        x_p = self.x ** 2 - self.x * self.t + self.y * self.t - self.x
        y_p = -self.y ** 2 - self.t ** 2 - self.x * self.y - self.x * self.t - self.y * self.t - self.y
        # Save the new coordinates
        self.coords = self.x, self.y = x_p, y_p
        return self.coords