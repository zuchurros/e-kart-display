import pygame
import math
import random
from settings import WIDTH
from settings import HEIGHT

# Setup
pygame.init()
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Speed Gauge")
clock = pygame.time.Clock()

# Colors
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
BAR_BG = (50, 50, 50)

# Parameters
bar_x, bar_y = 10, 10
bar_width, bar_height = 780, 80
max_speed = 120  # km/h


# Function to map speed to angle
def speed_to_angle(speed):
    angle_range = 270  # 135° to -135° (clockwise)
    angle = 135 - (speed / max_speed) * angle_range
    return math.radians(angle)

def get_bar_color(speed):
    ratio = speed / max_speed

    if ratio < 0.7:
        # Green to Yellow
        r = int(255 * (ratio / 0.7))
        g = 255
        b = 0
    elif ratio < 0.9:
        # Yellow zone (stay yellow)
        r = 255
        g = 255
        b = 0
    else:
        # Yellow to Red
        r = 255
        g = int(255 * ((1 - ratio) / 0.1))
        b = 0
    return (r, g, b)


def draw_speed_bar(screen, speed):
    # Clamp speed
    speed = max(0, min(speed, max_speed))

    # Calculate fill length
    fill_width = int((speed / max_speed) * bar_width)

    color = get_bar_color(speed)

    # Background bar
    pygame.draw.rect(screen, BAR_BG, (bar_x, bar_y, bar_width, bar_height), border_radius=10)

    # Fill bar
    pygame.draw.rect(screen, color, (bar_x, bar_y, fill_width, bar_height), border_radius=10)

    # Text
    font = pygame.font.Font("digital-7.ttf", 490)
    text = font.render(f"{int(speed)}", True, WHITE)
    screen.blit(text, (15, 100))
    font = pygame.font.Font("digital-7.ttf", 70)
    text = font.render(f"km/h", True, WHITE)
    screen.blit(text, (560, 280))