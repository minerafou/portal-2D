#import pygame
import pygame
from model.button import Button
from model.display_text import DisplayText

#class jeu
class Game():

    #fonction qui s'exucute quand game1 est cree
    def __init__(self, screen, screen_width, screen_height):

        #set les varioble
        #screen
        self.screen = screen
        self.screen_width = screen_width
        self.screen_height = screen_height

        #button menu
        self.menu_play_button = Button(200, 250, 800, 150, (180, 180, 180), (150, 150, 150), "Play", (0, 0, 0), 80)
        self.menu_editor_button = Button(200, 425, 800, 150, (180, 180, 180), (150, 150, 150), "Level Editor", (0, 0, 0), 80)
        self.menu_options_button = Button(200, 600, 800, 150, (180, 180, 180), (150, 150, 150), "Options", (0, 0, 0), 80)

        #text menu
        self.menu_game_name = DisplayText(20, 20, (0, 0, 0), "PORTAL 2D", 150)

        #game
        self.game_screen = "menu"

        #running variable
        self.running = True

    def CheckEvent(self):
        #verifie les evenement pygame
        for event in pygame.event.get():

            #check des input joueur
            #input de la croix rouge (en haut a droite de la fenetre)
            if event.type == pygame.QUIT:
                self.running = False

            #check le temps
            if event.type == pygame.USEREVENT:
                self.EveryTenMilliSecAction()

    def Refresh(self):
        #refresh l'ecran
        pygame.display.flip()

    def Update(self):
        #delete tous sur l'ecran
        self.screen.fill((220, 220, 220))

        #draw button
        self.menu_play_button.DrawButton(self.screen)
        self.menu_editor_button.DrawButton(self.screen)
        self.menu_options_button.DrawButton(self.screen)

        #draw text
        self.menu_game_name.DrawText(self.screen)

    def Run(self):
        #boucle global du jeu
        while self.running:
            self.CheckEvent()
            self.Update()
            self.Refresh()

    def EveryTenMilliSecAction(self):
        pass
    


