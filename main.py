import pygame
from constants import *
from player import Player
from asteroid import Asteroid
from asteroidfield import AsteroidField

def main():
    pygame.init()
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))

    player = Player(SCREEN_WIDTH / 2, SCREEN_HEIGHT / 2, PLAYER_RADIUS, "white")  # Create player object             

    print("Starting asteroids!")
    print(f"Screen width: {SCREEN_WIDTH}")
    print(f"Screen height: {SCREEN_HEIGHT}")

    updateable = pygame.sprite.Group()
    drawable = pygame.sprite.Group()
    asteroids = pygame.sprite.Group()

    Asteroid.containers = (asteroids, updateable, drawable)
    AsteroidField.containers = (updateable,)

    updateable.add(player)
    drawable.add(player)

    asteroid_field = AsteroidField()
    updateable.add(asteroid_field)

    clock = pygame.time.Clock()
    dt = 0

    running = True
    while running:
        screen.fill((0, 0, 0))
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
        
        updateable.update(dt)  # Update all updatables
        for drawable_obj in drawable:
            drawable_obj.draw(screen)  # Draw all drawables

        pygame.display.flip()  # Update the screen
        clock.tick(60)  # 60 FPS
        dt = clock.get_time() / 1000  # in seconds

if __name__ == "__main__":
    main()

