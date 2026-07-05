import pygame
from constants import SCREEN_WIDTH, SCREEN_HEIGHT
from logger import log_state
from player import Player
from asteroid import Asteroid
from asteroidfield import AsteroidField
from logger import log_event
import sys
from shot import Shot

def main():
    pygame.init()
    screen = pygame.display.set_mode((SCREEN_WIDTH,SCREEN_HEIGHT))
    print(f"Starting Asteroids with pygame version: {pygame.version.ver}")
    print(f"Screen width: {SCREEN_WIDTH}")
    print(f"Screen height: {SCREEN_HEIGHT}")
    clock = pygame.time.Clock()
    updatable = pygame.sprite.Group()
    drawable = pygame.sprite.Group()
    asteroids = pygame.sprite.Group()
    shots = pygame.sprite.Group()
    Shot.containers = (shots,drawable,updatable)
    AsteroidField.containers = (updatable)
    asteroid_field = AsteroidField()
    Asteroid.containers = (asteroids,updatable,drawable)
    Player.containers = (updatable,drawable)
    player = Player(x=SCREEN_WIDTH/2, y=SCREEN_HEIGHT/2)
    dt = 0.0
    while True:
        log_state()
        screen.fill("black")
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return
        
       
        for i in drawable:
            i.draw(screen)
        updatable.update(dt)
        for i in asteroids:
            if i.collides_with(player):
                log_event("player_hit")
                print("Game over!")
                sys.exit()
        for i in asteroids:
            for j in shots:
                if i.collides_with(j):
                    log_event("asteroid_shot")
                    i.split()
                    j.kill()
        pygame.display.flip()
        dt = clock.tick(60)/1000
        


if __name__ == "__main__":
    main()
