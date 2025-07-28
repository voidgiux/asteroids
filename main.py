import pygame
from constants import *

def main():
    pygame.init()
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
    while True:
        print("Starting Asteroids!")
        print(f"Screen width: {SCREEN_WIDTH}")
        print(f"Screen height: {SCREEN_HEIGHT}")
        screen.fill(SCREEN_COLOR, rect=None, special_flags=0) 
        pygame.display.flip()
        
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return 

if __name__ == "__main__":
    main()
