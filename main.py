import pygame

from constants import *

def main():
    pygame.init()
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))

    print("Starting asteroids!")
    print(f"Screen width: {SCREEN_WIDTH}")
    print(f"Screen height: {SCREEN_HEIGHT}")

    clock = pygame.time.Clock()
    dt = 0

    running = True
    while running:
        screen.fill((0, 0, 0))
        for event in pygame.event.get():    # User did something
            if event.type == pygame.QUIT:   # If user clicked close
                return
        pygame.display.flip()  # Update the screen
        clock.tick(60)  # 60 FPS
        dt = clock.get_time() / 1000  # in seconds

if __name__ == "__main__":
    main()

