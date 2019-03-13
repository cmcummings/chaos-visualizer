# utils.py
import time, random, pygame


def current_time_millis():
    return int(round(time.time() * 1000))


def random_color():
    r = random.randint(0, 255)
    g = random.randint(0, 255)
    b = random.randint(0, 255)
    return (r, g, b)
