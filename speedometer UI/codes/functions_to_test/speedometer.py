import pygame
import math
import random

# Setup
pygame.init()
WIDTH, HEIGHT = 480, 320
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Speed Gauge")
clock = pygame.time.Clock()

# Colors
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
BAR_BG = (50, 50, 50)

# Parameters
bar_x, bar_y = 10, 120
bar_width, bar_height = 460, 40
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
    font = pygame.font.Font("digital-7.ttf", 60)
    text = font.render(f"{int(speed)} km/h", True, WHITE)
    screen.blit(text, (bar_x + 145, bar_y - 50))


# Main loop
running = True
speed = 0

while running:
    screen.fill(BLACK)

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    # Simulate speed change
    #speed = random.uniform(0, max_speed)
    speed += 0.5
    if speed > max_speed:
        speed = 0

    draw_speed_bar(screen, speed)

    pygame.display.flip()
    clock.tick(20)  # Refresh rate

pygame.quit()
