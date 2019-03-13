# utils.py
import time, random, pygame, colorsys


def current_time_millis():
    """Gets the current time in milliseconds."""
    return int(round(time.time() * 1000))


def random_color():
    """Generates a random color tuple."""
    r = random.randint(0, 255)
    g = random.randint(0, 255)
    b = random.randint(0, 255)
    return (r, g, b)

def random_grayscale():
    """Generates a random grayscale color tuple."""
    x = random.randint(0, 255)
    return (x, x, x)

def round_to_place(x, place):
    """Rounds x."""
    return round(x*place)/place

def color_sequence(num, h=0):
    """Generates a continuous color spectrum."""
    colors = []

    s = 1
    v = 1
    for i in range(num):
        # Generate HSV value
        h += 1
        if h > 360:
            h = 0
        # Convert to RGB
        rgb = tuple(round(i * 255) for i in colorsys.hsv_to_rgb(h/360,s,v))
        colors.append(rgb)

    return colors