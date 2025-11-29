import pygame
import random


pygame.init()
WIDTH, HEIGHT = 480, 320
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Battery Display")
clock = pygame.time.Clock()

WHITE = (255, 255, 255)
GREEN = (0, 255, 0)
RED = (255, 0, 0)
YELLOW = (255, 255, 0)
BLACK = (0, 0, 0)

max_voltage = 12.6

font = pygame.font.SysFont(None, 36)

def draw_battery(voltage, charging):
    # Battery outline
    pygame.draw.rect(screen, WHITE, (50, 50, 200, 40), 3)  # Main body
    pygame.draw.rect(screen, WHITE, (250, 60, 10, 20))     # Battery tip

    # Voltage percentage (simulate 11.0V – 12.6V range)
    percent = voltage / max_voltage
    percent = max(0, min(percent, 1))  # Clamp 0–1
    bar_width = int(200 * percent)

    # Bar color
    color = GREEN if percent > 0.6 else YELLOW if percent > 0.2 else RED

    # Fill bar
    pygame.draw.rect(screen, color, (50, 50, bar_width, 40))

    # Voltage Text
    volt_text = font.render(f"{voltage:.2f}V", True, WHITE)
    screen.blit(volt_text, (50, 100))

    # Charging Status
    if charging:
        status_text = font.render("Charging...", True, GREEN)
    else:
        status_text = font.render("Not Charging", True, RED)
    screen.blit(status_text, (50, 140))



# Main loop
running = True
voltage = 12.6 #change voltage to read value fom sensor

while running:
    screen.fill(BLACK)

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    # Simulate random
    #voltage = random.uniform(11.0, 12.6)
    # charging = random.choice([True, False])


    # Simulate charging
    voltage += 0.1
    if voltage > 12.6:
       voltage = 0
    charging = True

    # Simulate on usage
    #voltage -= 0.1
    #if voltage < 0:
    #    voltage = 12.6
    #charging = False



    draw_battery(voltage, charging)

    pygame.display.flip()
    clock.tick(10)

pygame.quit()
