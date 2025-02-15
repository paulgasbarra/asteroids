import pygame
from constants import *
from player import Player
from asteroid import Asteroid
from asteroidfield import AsteroidField
from shot import Shot
from score import Score


def main():
    pygame.init()
    pygame.font.init()

    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
    clock = pygame.time.Clock()

    updatable = pygame.sprite.Group()
    drawable = pygame.sprite.Group()
    asteroids = pygame.sprite.Group()
    shots = pygame.sprite.Group()
    
    Asteroid.containers = (asteroids, updatable, drawable)
    AsteroidField.containers = updatable
    asteroid_field = AsteroidField()

    Shot.containers = (shots, updatable, drawable)
   
    Player.containers = (updatable, drawable)

    player = Player(SCREEN_WIDTH / 2, SCREEN_HEIGHT / 2)

    score = Score(SCREEN_WIDTH / 2, SCREEN_HEIGHT / 2)

    dt = 0

    

    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return
                
        updatable.update(dt)

        for asteroid in asteroids:
            if asteroid.did_collide_with(player):
                print("Game over!")
                return 
        
        for asteroid in asteroids:
            for shot in shots:
                if asteroid.did_collide_with(shot):
                    score.increase(asteroid)
                    asteroid.split()
                    shot.kill()

        screen.fill("black")

        for obj in drawable:
            obj.draw(screen)

        score.draw(screen)

        pygame.display.flip()

        dt = clock.tick(60) / 1000

if __name__ == "__main__":
    main()
   
   