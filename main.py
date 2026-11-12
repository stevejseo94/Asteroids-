import pygame
import random 
import sys
from asteroid import Asteroid
from asteroidfield import AsteroidField
from circleshape import CircleShape
from constants import (SCREEN_WIDTH , 
                       SCREEN_HEIGHT, 
                       ASTEROID_MIN_RADIUS, 
                       ASTEROID_MAX_RADIUS, 
                       STARTING_SCORE )  
from logger import log_state , log_event
from player import Player 
from shot import Shot 

def reset_game(asteroids, updatable, drawable, shots): 
    asteroids.empty() 
    updatable.empty()
    drawable.empty() 
    shots.empty() 

    player = Player(SCREEN_WIDTH / 2, SCREEN_HEIGHT / 2) 
    asteroidfield = AsteroidField()
    score_point = STARTING_SCORE 

    return player, asteroidfield, score_point 

def main():
    print(f"Starting Asteroids with pygame version {pygame.version.ver}")
    pygame.init()
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
    clock = pygame.time.Clock()
    dt = 0.0 

    score_font = pygame.font.SysFont("Arial", 20)
    game_pause_font = pygame.font.SysFont("Arial", 50)
    game_over_font = pygame.font.SysFont("Arial", 50)

    asteroids = pygame.sprite.Group()
    updatable = pygame.sprite.Group()
    drawable = pygame.sprite.Group()
    shots = pygame.sprite.Group()
    
    Player.containers = (updatable, drawable)
    Asteroid.containers = (asteroids, updatable, drawable)
    AsteroidField.containers = (updatable, )
    Shot.containers = (shots, updatable, drawable)
    
    player = Player(SCREEN_WIDTH / 2, SCREEN_HEIGHT / 2)
    asteroidfield = AsteroidField()
    score_point = STARTING_SCORE 

    explosion_sfx = pygame.mixer.Sound("/Users/steveseo/asteroids/sfx/mixkit-arcade-game-explosion-2759.wav")
    is_paused = False  
    game_over = False 

    while True:
        log_state()
        for event in pygame.event.get(): 
            if event.type == pygame.QUIT: 
                return 
            if not game_over: 
                if event.type == pygame.KEYDOWN and event.key == pygame.K_p: 
                    is_paused = True 
                if event.type == pygame.KEYDOWN and event.key == pygame.K_RETURN: 
                    is_paused = False
                if event.type == pygame.KEYDOWN and event.key == pygame.K_ESCAPE: 
                    return 
            else: 
                if event.type == pygame.KEYDOWN and event.key == pygame.K_RETURN: 
                    game_over = False 
                    is_paused = False 
                    player, asteroidfield, score_point = reset_game(asteroids, updatable, drawable, shots)
        
        if not game_over: 
            screen.fill("black")
            
            score_surface = score_font.render(f"Score: {score_point}", True, "white") 
            screen.blit(score_surface, (540, 0))

            for object in asteroids: 
                if CircleShape.collides_with(object, player) == True: 
                    log_event("player_hit")
                    explosion_sfx.play()
                    game_over = True 
                    game_over_surface = game_over_font.render("GAME OVER", True, "white")
                    screen.blit(game_over_surface, game_over_surface.get_rect(center=(SCREEN_WIDTH / 2, SCREEN_HEIGHT / 2)))
                    #sys.exit()        
            
            for asteroid in asteroids:
                for shot in shots: 
                    if asteroid.collides_with(shot): 
                        log_event("asteroid_shot")
                        if asteroid.radius == ASTEROID_MAX_RADIUS: 
                            score_point += 25
                        if asteroid.radius == ASTEROID_MAX_RADIUS - ASTEROID_MIN_RADIUS: 
                            score_point += 50
                        if asteroid.radius == ASTEROID_MIN_RADIUS: 
                            score_point += 100 
                        asteroid.split()
                        shot.kill()

            
            
            for object in drawable: 
                object.draw(screen) 

            if is_paused == True:
                game_paused_surface = game_pause_font.render("GAME PAUSED ||", True, "white")
                screen.blit(game_paused_surface, game_paused_surface.get_rect(center=(SCREEN_WIDTH / 2, SCREEN_HEIGHT / 2)))
            else: 
                updatable.update(dt)
            
            
            pygame.display.flip()
        
            dt = clock.tick(60) / 1000 
        
    




if __name__ == "__main__":
    main()
