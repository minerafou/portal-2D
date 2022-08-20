#import pygame et les differentes classes
import pygame
from model.game import Game

#initialize pygame
pygame.init()

#start un event toute les 10 milli sec
pygame.time.set_timer(pygame.USEREVENT, 10)

#set taille fenetre
screen_width = 1200

screen_height = 800

#set la fenetre
screen = pygame.display.set_mode((screen_width, screen_height))
pygame.display.set_caption("Portal 2D")

#cree le jeu a partir le l'objet 'game'
game1 = Game(screen, screen_width, screen_height)

#lance la boucle global
game1.Run()

#quitte pygame
pygame.quit()
