import pygame, sys 
from player import Player

class Game:
    """Class principale du jeu"""
    def __init__(self):
        player_sprite = Player((300,300))
        self.player = pygame.sprite.GroupSingle(player_sprite)

    def run(self):
        self.player.draw(screen)
        # Update all sprite groups
        # draw all sprite groups

if __name__ == '__main__':
    pygame.init()
    screen_with = 600
    screen_height = 600
    screen = pygame.display.set_mode((screen_with,screen_height))
    clock = pygame.time.Clock()
    game = Game()

    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()

        screen.fill((30,30,30))
        game.run()

        pygame.display.flip()
        clock.tick(60)
