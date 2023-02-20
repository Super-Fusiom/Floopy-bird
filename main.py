import pygame
from pygame.locals import *

def main():
    #Initialise the screen
    pygame.init()
    screen = pygame.display.set_mode((150, 50))
    pygame.display.set_caption('Floopy Bird')
    # Background
    background = pygame.Surface(screen.get_size())
    background = background.convert()
    background.fill((250, 250, 250))

    # Text
    font = pygame.font.Font(None, 36)
    text = font.render("Floopy Bird", 1, (10,10,10))
    textpos = text.get_rect()
    textpos.centerx = background.get_rect().centerx
    background.blit(text, textpos)

    # Blit
    screen.blit(background, (0,0))
    pygame.display.flip()

    # Event loop
    while True:
        for event in pygame.event.get():
            if event.type == QUIT:
                return
        
        screen.blit(background, (0,0))
        pygame.display.flip()


    
if __name__ == '__main__': main()



