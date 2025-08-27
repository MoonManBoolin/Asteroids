import pygame
from constants import *
from player import Player
from asteroid import Asteroid
from asteroidfield import AsteroidField
from shot import Shot

def main():
    print("Starting Asteroids!")
    print(f"Screen width: {SCREEN_WIDTH}")
    print(f"Screen height: {SCREEN_HEIGHT}")
    lives = 3
    print("----------------------------")
    print(f"Total lives: {lives}")
    pygame.init()
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
    clock = pygame.time.Clock()
    dt = 0
    updatable = pygame.sprite.Group()
    drawable = pygame.sprite.Group()
    asteroids = pygame.sprite.Group()
    shots = pygame.sprite.Group()
    Shot.containers = (shots, updatable, drawable)
    AsteroidField.containers = (updatable)
    Asteroid.containers = (asteroids, updatable, drawable)
    Player.containers = (updatable, drawable)
    player = Player(SCREEN_WIDTH / 2, SCREEN_HEIGHT / 2)
    field = AsteroidField()
    score = 0
    
    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return
        pygame.Surface.fill(screen, (0,0,0))
        updatable.update(dt)
        for i in drawable:
            i.draw(screen)
        pygame.display.flip()
        dt = clock.tick(60) / 1000
        for i in asteroids:
            if (i.collision(player) <= (i.radius + player.radius)):
                if (lives <= 0):
                    print("-----------------------")
                    print("Game over!")
                    print(f"Your score: {score}")
                    return
                lives -= 1
                print("-----------------------")
                print("Uh-Oh, you died!")
                print("")
                print(f"Lives remaining: {lives}")
                print(f"Current score: {score}")
                for g in (updatable, drawable, asteroids, shots):
                    g.empty()
                player = Player(SCREEN_WIDTH / 2, SCREEN_HEIGHT / 2)
                field = AsteroidField()
                
        for obj1 in asteroids:
            for obj2 in shots:
                if (obj1.collision(obj2) <= (obj1.radius + obj2.radius)):
                    score += 1
                    obj1.split()
                    obj2.kill()

if __name__ == "__main__":
    main()
