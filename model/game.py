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
        self.menu_play_button = Button(150, 250, 900, 150, (180, 180, 180), (150, 150, 150), "Play", (0, 0, 0), 80)
        self.menu_editor_button = Button(150, 425, 900, 150, (180, 180, 180), (150, 150, 150), "Level Editor", (0, 0, 0), 80)
        self.menu_options_button = Button(150, 600, 425, 150, (180, 180, 180), (150, 150, 150), "Options", (0, 0, 0), 80)
        self.menu_quit_button = Button(625, 600, 425, 150, (180, 180, 180), (150, 150, 150), "Quit", (0, 0, 0), 80)

        #text menu
        self.menu_game_name = DisplayText(120, 20, (32, 111, 247), "PORTAL", 150)
        self.menu_game_name2 = DisplayText(850, 20, (235, 132, 29), "2D", 150)

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
            
            #input de la souris
            if event.type == pygame.MOUSEBUTTONDOWN:
                
                #check des buttons
                self.check_button()

    def Refresh(self):
        #refresh l'ecran
        pygame.display.flip()

    def Update(self):
        #delete tous sur l'ecran
        self.screen.fill((220, 220, 220))

        if self.game_screen == "menu":
            self.UpdateMenu()

    def Run(self):
        #boucle global du jeu
        while self.running:
            self.CheckEvent()
            self.Update()
            self.Refresh()

    def EveryTenMilliSecAction(self):
        pass

    def UpdateMenu(self):
        #draw button
        self.menu_play_button.DrawButton(self.screen)
        self.menu_editor_button.DrawButton(self.screen)
        self.menu_options_button.DrawButton(self.screen)
        self.menu_quit_button.DrawButton(self.screen)

        #draw text
        self.menu_game_name.DrawText(self.screen)
        self.menu_game_name2.DrawText(self.screen)

    def check_button(self):
        if self.game_screen == "menu":
            if self.menu_play_button.IsPressed():
                pass
            elif self.menu_editor_button.IsPressed():
                pass
            elif self.menu_options_button.IsPressed():
                pass
            elif self.menu_quit_button.IsPressed():
                self.running = False


    


