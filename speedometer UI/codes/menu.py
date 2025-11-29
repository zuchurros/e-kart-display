import pygame

pygame.init()
WIDTH, HEIGHT = 480, 320
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("E-Kart Menu Example")
clock = pygame.time.Clock()
font = pygame.font.SysFont(None, 40)

# Track which screen is showing
current_screen = "main"

# Draw functions for each screen
def draw_main(screen):
    screen.fill((0, 0, 50))
    text = font.render("Main Dashboard", True, (255, 255, 255))
    screen.blit(text, (120, 140))

def draw_settings(screen):
    screen.fill((20, 20, 20))
    text = font.render("Settings", True, (0, 255, 0))
    screen.blit(text, (180, 140))

def draw_diagnostics(screen):
    screen.fill((50, 0, 0))
    text = font.render("Diagnostics", True, (255, 100, 100))
    screen.blit(text, (150, 140))

def draw_speed_bar(screen, speed):
        # Clamp speed
        speed = max(0, min(speed, max_speed))

        # Calculate fill length
        fill_width = int((speed / max_speed) * bar_width)

        # Background bar
        pygame.draw.rect(screen, BAR_BG, (bar_x, bar_y, bar_width, bar_height), border_radius=10)

        # Fill bar
        pygame.draw.rect(screen, BAR_FILL, (bar_x, bar_y, fill_width, bar_height), border_radius=10)

        # Text
        text = font.render(f"Speed: {speed:.1f} km/h", True, WHITE)
        screen.blit(text, (bar_x, bar_y - 40))

running = True

while running:
    screen.fill((0, 0, 0))

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

        # Key press to switch menus
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_1:
                current_screen = "main"
            elif event.key == pygame.K_2:
                current_screen = "settings"
            elif event.key == pygame.K_3:
                current_screen = "diagnostics"

    # Draw the current screen
    if current_screen == "main":
        draw_main(screen)
    elif current_screen == "settings":
        draw_settings(screen)
    elif current_screen == "diagnostics":
        draw_diagnostics(screen)

    pygame.display.flip()
    clock.tick(30)

pygame.quit()
