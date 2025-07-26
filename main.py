import pygame
from constants import *
from player import Player
from asteroid import Asteroid
from asteroidfield import AsteroidField
from shot import Shot

def main():
    pygame.init()
    print("Starting Asteroids!")

    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
    clock = pygame.time.Clock()
    dt = 0

    # === Sprite Groups ===
    updatable = pygame.sprite.Group()
    drawable = pygame.sprite.Group()
    asteroids = pygame.sprite.Group()
    shots = pygame.sprite.Group()

    # === Assign static containers ===
    Player.containers = updatable, drawable
    Asteroid.containers = asteroids, updatable, drawable
    Shot.containers = shots, updatable, drawable
    AsteroidField.containers = (updatable,)

    # === Create game objects ===
    player = Player(SCREEN_WIDTH / 2, SCREEN_HEIGHT / 2, PLAYER_RADIUS)
    asteroid_field = AsteroidField()

    # === Game Loop ===
    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return

        screen.fill("black")

        # Update all game objects
        updatable.update(dt)

        # Collision detection (player-asteroid)
        for asteroid in asteroids:
            if player.checkCollision(asteroid):
                print("Game over!")
                pygame.quit()
                exit()

        # Collision between shot and asteroid
        for asteroid in asteroids:
            for shot in shots:
                if asteroid.checkCollision(shot):
                    asteroid.split()
                    shot.kill() 

        # Draw all drawable objects (player, asteroids, shots)
        for obj in drawable:
            obj.draw(screen)

        pygame.display.flip()
        dt = clock.tick(60) / 1000  # Convert to seconds

if __name__ == "__main__":
    main()
