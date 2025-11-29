import pygame
from battvert_func_only import draw_vertical_bar
# from edit import draw_vertical_bar
from speedometer_func_only import draw_speed_bar
from settings import WIDTH
from settings import HEIGHT

pygame.init()
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("eKart Dashboard")
clock = pygame.time.Clock()
font = pygame.font.SysFont(None, 32)
bolt_img = pygame.image.load("bolt.png").convert_alpha()
bolt_img = pygame.transform.scale(bolt_img, (60, 90))  # Resize if needed

# Values
speed = 0
battery = 0
max_speed = 120
max_batt = 12.6
charging = True

running = True
while running:
    screen.fill((0, 0, 0))

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    # Simulate values
    speed += 0.3
    if speed > max_speed:
        speed = 0

    if charging:
        battery += 0.05

        if battery >= max_batt:
            battery = max_batt
            charging = False
            continue


    else:
        battery -= 0.05

        if battery <= 0:
            # battery = 0
            charging = True
            continue




    # Draw bars
    draw_speed_bar(screen, speed)
    draw_vertical_bar(screen, WIDTH - 60, 360, 50, 90, battery, max_batt, "", charging,bolt_img)

    pygame.display.flip()
    clock.tick(60)

pygame.quit()

