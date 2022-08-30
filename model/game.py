#import pygame
import pygame
import pyperclip
from model.button import Button, ButtonEditor
from model.display_text import DisplayText
from model.level import *

#class jeu
class Game():

    #fonction qui s'exucute quand game1 est cree
    def __init__(self, screen, screen_width, screen_height):

        #set les varioble
        #screen
        pyperclip.copy('The text to be copied to the clipboard.')
        self.screen = screen
        self.screen_width = screen_width
        self.screen_height = screen_height

        #button menu
        self.menu_play_button = Button(150, 250, 900, 150, (180, 180, 180), (150, 150, 150), "Play", (0, 0, 0), 70)
        self.menu_editor_button = Button(150, 425, 900, 150, (180, 180, 180), (150, 150, 150), "Level Editor", (0, 0, 0), 70)
        self.menu_options_button = Button(150, 600, 425, 150, (180, 180, 180), (150, 150, 150), "Options", (0, 0, 0), 70)
        self.menu_quit_button = Button(625, 600, 425, 150, (180, 180, 180), (150, 150, 150), "Quit", (0, 0, 0), 70)

        #text menu
        self.menu_game_name = DisplayText(120, 20, (32, 111, 247), "PORTAL", 150)
        self.menu_game_name2 = DisplayText(850, 20, (235, 132, 29), "2D", 150)

        #button playing scene
        self.playing_scene_back_button = Button(0, 0, 200, 80, (180, 180, 180), (150, 150, 150), "Back", (0, 0, 0), 40)

        #button level selection
        self.level_selection_back_button = Button(100, 650, 1000, 100, (180, 180, 180), (150, 150, 150), "Back", (0, 0, 0), 40)

        self.level_selection_1 = Button(100, 200, 100, 100, (180, 180, 180), (150, 150, 150), "1", (0, 0, 0), 40)
        self.level_selection_2 = Button(250, 200, 100, 100, (180, 180, 180), (150, 150, 150), "2", (0, 0, 0), 40)
        self.level_selection_3 = Button(400, 200, 100, 100, (180, 180, 180), (150, 150, 150), "3", (0, 0, 0), 40)
        self.level_selection_4 = Button(550, 200, 100, 100, (180, 180, 180), (150, 150, 150), "4", (0, 0, 0), 40)
        self.level_selection_5 = Button(700, 200, 100, 100, (180, 180, 180), (150, 150, 150), "5", (0, 0, 0), 40)
        self.level_selection_6 = Button(850, 200, 100, 100, (180, 180, 180), (150, 150, 150), "6", (0, 0, 0), 40)
        self.level_selection_7 = Button(1000, 200, 100, 100, (180, 180, 180), (150, 150, 150), "7", (0, 0, 0), 40)
        self.level_selection_8 = Button(100, 350, 100, 100, (180, 180, 180), (150, 150, 150), "8", (0, 0, 0), 40)
        self.level_selection_9 = Button(250, 350, 100, 100, (180, 180, 180), (150, 150, 150), "9", (0, 0, 0), 40)
        self.level_selection_10 = Button(400, 350, 100, 100, (180, 180, 180), (150, 150, 150), "10", (0, 0, 0), 40)
        self.level_selection_11 = Button(550, 350, 100, 100, (180, 180, 180), (150, 150, 150), "11", (0, 0, 0), 40)
        self.level_selection_12 = Button(700, 350, 100, 100, (180, 180, 180), (150, 150, 150), "12", (0, 0, 0), 40)
        self.level_selection_13 = Button(850, 350, 100, 100, (180, 180, 180), (150, 150, 150), "13", (0, 0, 0), 40)
        self.level_selection_14 = Button(1000, 350, 100, 100, (180, 180, 180), (150, 150, 150), "14", (0, 0, 0), 40)

        #text playing scene
        self.playing_scene_level = DisplayText(230, 10, (0, 0, 0), "None (le text et modif apres)", 50)
        self.playing_scene_time = DisplayText(550, 10, (0, 0, 0), "None (le text et modif apres)", 50)

        #text for level selection
        self.level_selection_text = DisplayText(150, 20, (0, 0, 0), "Select a level", 100)

        #text win screen
        self.win_screen_title = DisplayText(70, 10, (0, 0, 0), "You win", 200)
        self.win_screen_subtitle = DisplayText(260, 250, (120, 120, 120), "Well played", 80)

        #button win screen
        self.win_screen_next = Button(650, 500, 450, 200, (180, 180, 180), (150, 150, 150), "Next", (0, 0, 0), 120)
        self.win_screen_back = Button(100, 500, 450, 200, (180, 180, 180), (150, 150, 150), "Back", (0, 0, 0), 120)

        #button editor (and for playing scene for the fisrt)
        self.editor_playing_scene_help = Button(1120, 0, 80, 80, (180, 180, 180), (150, 150, 150), "?", (0, 0, 0), 40)
        self.editor_play = Button(970, 0, 150, 80, (180, 180, 180), (150, 150, 150), "play", (0, 0, 0), 40)

        self.editor_mur_button = ButtonEditor(220, 20, 40, 40, "mur")
        self.editor_lav_button = ButtonEditor(280, 20, 40, 40, "lav")
        self.editor_res_button = ButtonEditor(340, 20, 40, 40, "res")
        self.editor_mlu_button = ButtonEditor(400, 20, 40, 40, "mlu")
        self.editor_mld_button = ButtonEditor(460, 20, 40, 40, "mld")
        self.editor_owu_button = ButtonEditor(520, 20, 40, 40, "owu")
        self.editor_owd_button = ButtonEditor(580, 20, 40, 40, "owd")
        self.editor_owl_button = ButtonEditor(640, 20, 40, 40, "owl")
        self.editor_owr_button = ButtonEditor(700, 20, 40, 40, "owr")
        self.editor_fin_button = ButtonEditor(760, 20, 40, 40, "fin")
        self.editor_ply_button = ButtonEditor(820, 20, 40, 40, "ply")

        #vadil level text
        self.valid_level_text = DisplayText(220, 18, (0, 0, 0), "Please finish you're level", 40)

        #game
        self.game_screen = "menu"
        self.player_position_x = 2
        self.player_position_y = 2
        self.lvl_width = 30
        self.lvl_height = 18
        self.tile_width = 40
        self.tile_height = 40
        self.portal_orange = [0, 0, 0]
        self.portal_blue = [0, 0, 0]
        self.level_number = 0
        self.counter = 0
        self.seconde = 0
        self.selected = "air"

        #running variable
        self.running = True

        #set a default level
        self.level_default = GetLevel(1)

        #copy pour les modif
        self.level = self.level_default.copy()
    
    def SetLevel(self, level_num):
        self.level_number = level_num
        self.ResetPortal()
        self.ResetSeconde()
        new_level = GetLevel(level_num)
        player_index = new_level.index("ply")
        self.player_position_x = player_index % self.lvl_width
        self.player_position_y = player_index // self.lvl_width
        self.playing_scene_level.SetText("Level: " + str(self.level_number))
        return new_level
    
    def CheckEvent(self):

        #check la win
        if self.game_screen == "playing scene":
            if self.level[self.player_position_x + (self.player_position_y * self.lvl_width)] == "fin":
                self.game_screen = "win screen"
            
        if self.game_screen == "valid level":
            if self.level[self.player_position_x + (self.player_position_y * self.lvl_width)] == "fin":
                pyperclip.copy(str(self.level))
                self.game_screen = "valid screen"

        #check res portal
        if self.game_screen == "playing scene":
            if self.level[self.player_position_x + (self.player_position_y * self.lvl_width)] == "res":
                self.ResetPortal()

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
                if event.button == 1:
                    #left
                    #check des buttons
                    if self.game_screen == "playing scene" or self.game_screen == "valid level":
                        self.SendPortal("blue")
                    elif self.game_screen == "editor":
                        self.PosBlock()
                    
                    self.CheckButton()

                elif event.button == 3:
                    #right
                    if self.game_screen == "playing scene" or self.game_screen == "valid level":
                        self.SendPortal("orange")
                    elif self.game_screen == "editor":
                        self.DelBlock()

            #check input clavier
            if self.game_screen == "playing scene" or self.game_screen == "valid level":
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_z:
                        self.MovePlayer("up")
                    if event.key == pygame.K_q:
                        self.MovePlayer("left")
                    if event.key == pygame.K_s:
                        self.MovePlayer("down")
                    if event.key == pygame.K_d:
                        self.MovePlayer("right")

    def Refresh(self):
        #refresh l'ecran
        pygame.display.flip()

    def Update(self):
        #delete tous sur l'ecran
        self.screen.fill((220, 220, 220))

        
        if self.game_screen == "playing scene":
            self.UpdatePlayingScene()
        
        elif self.game_screen == "menu":
            self.UpdateMenu()

        elif self.game_screen == "level selection":
            self.UpdateLevelSelection()

        elif self.game_screen == "win screen":
            self.UpdateWinScreen()
        
        elif self.game_screen == "editor":
            self.UpdateEditor()

        elif self.game_screen == "editor help":
            self.UpdateEditorHelp()
        
        elif self.game_screen == "play help":
            self.UpdatePlayHelp()

        elif self.game_screen == "valid level":
            self.UpdateValidLevel()

        elif self.game_screen == "valid screen":
            self.UpdateValidScreen()

    def Run(self):
        #boucle global du jeu
        while self.running:
            self.CheckEvent()
            self.Update()
            self.Refresh()

    def EveryTenMilliSecAction(self):
        self.counter += 1
        if self.counter == 100:
            self.counter = 0
            self.seconde += 1

    def UpdateMenu(self):
        #draw button
        self.menu_play_button.DrawButton(self.screen)
        self.menu_editor_button.DrawButton(self.screen)
        self.menu_options_button.DrawButton(self.screen)
        self.menu_quit_button.DrawButton(self.screen)

        #draw text
        self.menu_game_name.DrawText(self.screen)
        self.menu_game_name2.DrawText(self.screen)

    def UpdatePlayingScene(self):
        #draw text
        self.playing_scene_level.DrawText(self.screen)

        self.playing_scene_time.SetText(self.SetTime(self.seconde))
        self.playing_scene_time.DrawText(self.screen)
        
        #draw button
        self.playing_scene_back_button.DrawButton(self.screen)
        self.editor_playing_scene_help.DrawButton(self.screen)

        #draw level
        self.DrawLevel()

        #draw player
        self.DrawPlayer()

        #draw portals
        self.DrawPortals()
    
    def UpdateLevelSelection(self):
        #draw button
        self.level_selection_back_button.DrawButton(self.screen)

        self.level_selection_1.DrawButton(self.screen)
        self.level_selection_2.DrawButton(self.screen)
        self.level_selection_3.DrawButton(self.screen)
        self.level_selection_4.DrawButton(self.screen)
        self.level_selection_5.DrawButton(self.screen)
        self.level_selection_6.DrawButton(self.screen)
        self.level_selection_7.DrawButton(self.screen)
        self.level_selection_8.DrawButton(self.screen)
        self.level_selection_9.DrawButton(self.screen)
        self.level_selection_10.DrawButton(self.screen)
        self.level_selection_11.DrawButton(self.screen)
        self.level_selection_12.DrawButton(self.screen)
        self.level_selection_13.DrawButton(self.screen)
        self.level_selection_14.DrawButton(self.screen)

        #draw text
        self.level_selection_text.DrawText(self.screen)

    def UpdateWinScreen(self):
        #draw button
        self.win_screen_next.DrawButton(self.screen)
        self.win_screen_back.DrawButton(self.screen)

        #draw text
        self.win_screen_title.DrawText(self.screen)
        self.win_screen_subtitle.DrawText(self.screen)

    def UpdateEditor(self):

        #draw button
        self.playing_scene_back_button.DrawButton(self.screen)
        self.editor_lav_button.DrawButton(self.screen)
        self.editor_res_button.DrawButton(self.screen)
        self.editor_mur_button.DrawButton(self.screen)
        self.editor_mlu_button.DrawButton(self.screen)
        self.editor_mld_button.DrawButton(self.screen)
        self.editor_owu_button.DrawButton(self.screen)
        self.editor_owd_button.DrawButton(self.screen)
        self.editor_owl_button.DrawButton(self.screen)
        self.editor_owr_button.DrawButton(self.screen)
        self.editor_fin_button.DrawButton(self.screen)
        self.editor_ply_button.DrawButton(self.screen)

        self.editor_playing_scene_help.DrawButton(self.screen)
        self.editor_play.DrawButton(self.screen)

        #draw level
        self.DrawLevel()

        #set player pos
        self.SetPlayerPos()

        #draw player
        if "ply" in self.level:
            self.DrawPlayer()

        #draw selected tile
        self.DrawSelectedTile()

    def UpdatePlayHelp(self):
        #draw button
        self.level_selection_back_button.DrawButton(self.screen)

    def UpdateEditorHelp(self):
        #draw button
        self.level_selection_back_button.DrawButton(self.screen)

    def UpdateValidLevel(self):

        #draw button
        self.playing_scene_back_button.DrawButton(self.screen)

        #draw text
        self.valid_level_text.DrawText(self.screen)

        #draw level
        self.DrawLevel()

        #draw player
        self.DrawPlayer()

        #draw portals
        self.DrawPortals()

    def UpdateValidScreen(self):
        #draw button
        self.level_selection_back_button.DrawButton(self.screen)

    def CheckButton(self):
        #for menu screen
        if self.game_screen == "menu":
            if self.menu_play_button.IsPressed():
                self.game_screen = "level selection"
            elif self.menu_editor_button.IsPressed():
                self.game_screen = "editor"

                #set a black level
                self.level = CreateLevel(self.lvl_width, self.lvl_height)
            elif self.menu_options_button.IsPressed():
                pass
            elif self.menu_quit_button.IsPressed():
                self.running = False

        #for playing screen
        elif self.game_screen == "playing scene":
            if self.playing_scene_back_button.IsPressed():
                self.game_screen = "level selection"
            elif self.editor_playing_scene_help.IsPressed():
                self.game_screen = "play help"
            
        #for win screen
        elif self.game_screen == "win screen":
            if self.win_screen_back.IsPressed():
                self.game_screen = "level selection"
            elif self.win_screen_next.IsPressed():
                self.level = self.SetLevel(self.level_number + 1)
                self.game_screen = "playing scene"
        
        #for help editor
        elif self.game_screen == "editor help":
            if self.level_selection_back_button.IsPressed():
                self.game_screen = "editor"
        
        #for help play
        elif self.game_screen == "play help":
            if self.level_selection_back_button.IsPressed():
                self.game_screen = "playing scene"
            
        #for valid level
        elif self.game_screen == "valid level":
            if self.playing_scene_back_button.IsPressed():
                self.game_screen = "editor"

        #for valid screen
        elif self.game_screen == "valid screen":
            if self.level_selection_back_button.IsPressed():
                self.game_screen = "editor"

        #for editor
        elif self.game_screen == "editor":
            if self.playing_scene_back_button.IsPressed():
                self.game_screen = "menu"
            elif self.editor_playing_scene_help.IsPressed():
                self.game_screen = "editor help"
            elif self.editor_play.IsPressed():
                #check if player is in the level
                if "ply" in self.level:
                    self.game_screen = "valid level"
                    self.ResetPortal()
                else:
                    pass
            elif self.editor_lav_button.IsPressed():
                self.selected = "lav"
            elif self.editor_res_button.IsPressed():
                self.selected = "res"
            elif self.editor_mlu_button.IsPressed():
                self.selected = "mlu"
            elif self.editor_mld_button.IsPressed():
                self.selected = "mld"
            elif self.editor_owu_button.IsPressed():
                self.selected = "owu"
            elif self.editor_owd_button.IsPressed():
                self.selected = "owd"
            elif self.editor_owl_button.IsPressed():
                self.selected = "owl"
            elif self.editor_owr_button.IsPressed():
                self.selected = "owr"
            elif self.editor_fin_button.IsPressed():
                self.selected = "fin"
            elif self.editor_mur_button.IsPressed():
                self.selected = "mur"
            elif self.editor_ply_button.IsPressed():
                self.selected = "ply"


        #for level selection
        elif self.game_screen == "level selection":
            if self.level_selection_back_button.IsPressed():
                self.game_screen = "menu"    

            elif self.level_selection_1.IsPressed():
                self.level = self.SetLevel(1)
                self.game_screen = "playing scene"
            elif self.level_selection_2.IsPressed():
                self.level = self.SetLevel(2)
                self.game_screen = "playing scene"
            elif self.level_selection_3.IsPressed():
                self.level = self.SetLevel(3)
                self.game_screen = "playing scene"
            elif self.level_selection_4.IsPressed():
                self.level = self.SetLevel(4)
                self.game_screen = "playing scene"
            elif self.level_selection_5.IsPressed():
                self.level = self.SetLevel(5)
                self.game_screen = "playing scene"
            elif self.level_selection_6.IsPressed():
                self.level = self.SetLevel(6)
                self.game_screen = "playing scene"
            elif self.level_selection_7.IsPressed():
                self.level = self.SetLevel(7)
                self.game_screen = "playing scene"
            elif self.level_selection_8.IsPressed():
                self.level = self.SetLevel(8)
                self.game_screen = "playing scene"
            elif self.level_selection_9.IsPressed():
                self.level = self.SetLevel(9)
                self.game_screen = "playing scene"
            elif self.level_selection_10.IsPressed():
                self.level = self.SetLevel(10)
                self.game_screen = "playing scene"
            elif self.level_selection_11.IsPressed():
                self.level = self.SetLevel(11)
                self.game_screen = "playing scene"
            elif self.level_selection_12.IsPressed():
                self.level = self.SetLevel(12)
                self.game_screen = "playing scene"
            elif self.level_selection_13.IsPressed():
                self.level = self.SetLevel(13)
                self.game_screen = "playing scene"
            elif self.level_selection_14.IsPressed():
                self.level = self.SetLevel(14)
                self.game_screen = "playing scene"
         
    def DrawLevel(self):
        for i in range(self.lvl_width * self.lvl_height):
            tile_x = ((i % self.lvl_width) * self.tile_width)
            tile_y = ((i // self.lvl_width) * self.tile_height) + 80
            tile_rect = pygame.Rect(tile_x, tile_y, self.tile_width, self.tile_height)
            mlu_points = [(tile_x + 30, tile_y + 1), (tile_x + 38, tile_y + 1), (tile_x + 38, tile_y + 10),
                          (tile_x + 10, tile_y + 38), (tile_x + 1, tile_y + 38), (tile_x + 1, tile_y + 30)]
            mld_points = [(tile_x + 1, tile_y + 1), (tile_x + 10, tile_y + 1), (tile_x + 38, tile_y + 29),
                          (tile_x + 38, tile_y + 38), (tile_x + 29, tile_y + 38), (tile_x + 1, tile_y + 10)]

            owu_points = [(tile_x + 19, tile_y + 11), (tile_x + 20, tile_y + 11), (tile_x + 30, tile_y + 21),
                          (tile_x + 25, tile_y + 21), (tile_x + 25, tile_y + 31), (tile_x + 14, tile_y + 31),
                          (tile_x + 14, tile_y + 21), (tile_x + 9, tile_y + 21)]
            owd_points = [(tile_x + 20, tile_y + 28), (tile_x + 19, tile_y + 28), (tile_x + 9, tile_y + 18),
                          (tile_x + 14, tile_y + 18), (tile_x + 14, tile_y + 8), (tile_x + 25, tile_y + 8),
                          (tile_x + 25, tile_y + 18), (tile_x + 30, tile_y + 18)]
            owr_points = [(tile_x + 28, tile_y + 19), (tile_x + 28, tile_y + 20), (tile_x + 18, tile_y + 30),
                          (tile_x + 18, tile_y + 25), (tile_x + 8, tile_y + 25), (tile_x + 8, tile_y + 14),
                          (tile_x + 18, tile_y + 14), (tile_x + 18, tile_y + 9)]
            owl_points = [(tile_x + 11, tile_y + 19), (tile_x + 11, tile_y + 20), (tile_x + 21, tile_y + 30),
                          (tile_x + 21, tile_y + 25), (tile_x + 31, tile_y + 25), (tile_x + 31, tile_y + 14),
                          (tile_x + 21, tile_y + 14), (tile_x + 21, tile_y + 9)]
            if self.level[i] == "mur":
                pygame.draw.rect(self.screen, (100, 100, 100), tile_rect)

            elif self.level[i] == "air":
                pygame.draw.rect(self.screen, (180, 180, 180), tile_rect)
                tile_rect = pygame.Rect(tile_x + 2, tile_y + 2, self.tile_width - 4, self.tile_height - 4)
                pygame.draw.rect(self.screen, (220, 220, 220), tile_rect)

            elif self.level[i] == "ply":
                pygame.draw.rect(self.screen, (180, 180, 180), tile_rect)
                tile_rect = pygame.Rect(tile_x + 2, tile_y + 2, self.tile_width - 4, self.tile_height - 4)
                pygame.draw.rect(self.screen, (220, 220, 220), tile_rect)

            elif self.level[i] == "fin":
                pygame.draw.rect(self.screen, (180, 180, 180), tile_rect)
                tile_rect = pygame.Rect(tile_x + 2, tile_y + 2, self.tile_width - 4, self.tile_height - 4)
                pygame.draw.rect(self.screen, (255, 195, 0), tile_rect)

            elif self.level[i] == "lav":
                pygame.draw.rect(self.screen, (255, 77, 0), tile_rect)

            elif self.level[i] == "res":
                pygame.draw.rect(self.screen, (73, 163, 194), tile_rect)
                tile_rect = pygame.Rect(tile_x + 2, tile_y + 2, self.tile_width - 4, self.tile_height - 4)
                pygame.draw.rect(self.screen, (95, 191, 224), tile_rect)

            elif self.level[i] == "mlu":
                pygame.draw.rect(self.screen, (180, 180, 180), tile_rect)
                tile_rect = pygame.Rect(tile_x + 2, tile_y + 2, self.tile_width - 4, self.tile_height - 4)
                pygame.draw.rect(self.screen, (220, 220, 220), tile_rect)
                pygame.draw.lines(self.screen, (0, 0, 0), 1, mlu_points, 3)
                pygame.draw.line(self.screen, (0, 0, 0), (tile_x , tile_y + 39), (tile_x + 39, tile_y), 2)

            elif self.level[i] == "mld":
                pygame.draw.rect(self.screen, (180, 180, 180), tile_rect)
                tile_rect = pygame.Rect(tile_x + 2, tile_y + 2, self.tile_width - 4, self.tile_height - 4)
                pygame.draw.rect(self.screen, (220, 220, 220), tile_rect)
                pygame.draw.lines(self.screen, (0, 0, 0), 1, mld_points, 3)
                pygame.draw.line(self.screen, (0, 0, 0), (tile_x, tile_y), (tile_x + 39, tile_y + 39), 2)
            
            elif self.level[i] == "owu":
                pygame.draw.rect(self.screen, (180, 180, 180), tile_rect)
                tile_rect = pygame.Rect(tile_x + 2, tile_y + 2, self.tile_width - 4, self.tile_height - 4)
                pygame.draw.rect(self.screen, (200, 200, 200), tile_rect)
                tile_rect = pygame.Rect(tile_x + 2, tile_y + 2, self.tile_width - 4, self.tile_height - 34)
                pygame.draw.rect(self.screen, (160, 160, 160), tile_rect)
                pygame.draw.lines(self.screen, (250, 54, 31), 1, owu_points, 3)

            elif self.level[i] == "owd":
                pygame.draw.rect(self.screen, (180, 180, 180), tile_rect)
                tile_rect = pygame.Rect(tile_x + 2, tile_y + 2, self.tile_width - 4, self.tile_height - 4)
                pygame.draw.rect(self.screen, (200, 200, 200), tile_rect)
                tile_rect = pygame.Rect(tile_x + 2, tile_y + 32, self.tile_width - 4, self.tile_height - 34)
                pygame.draw.rect(self.screen, (160, 160, 160), tile_rect)
                pygame.draw.lines(self.screen, (250, 54, 31), 1, owd_points, 3)

            elif self.level[i] == "owl":
                pygame.draw.rect(self.screen, (180, 180, 180), tile_rect)
                tile_rect = pygame.Rect(tile_x + 2, tile_y + 2, self.tile_width - 4, self.tile_height - 4)
                pygame.draw.rect(self.screen, (200, 200, 200), tile_rect)
                tile_rect = pygame.Rect(tile_x + 2, tile_y + 2, self.tile_width - 34, self.tile_height - 4)
                pygame.draw.rect(self.screen, (160, 160, 160), tile_rect)
                pygame.draw.lines(self.screen, (250, 54, 31), 1, owl_points, 3)

            elif self.level[i] == "owr":
                pygame.draw.rect(self.screen, (180, 180, 180), tile_rect)
                tile_rect = pygame.Rect(tile_x + 2, tile_y + 2, self.tile_width - 4, self.tile_height - 4)
                pygame.draw.rect(self.screen, (200, 200, 200), tile_rect)
                tile_rect = pygame.Rect(tile_x + 32, tile_y + 2, self.tile_width - 34, self.tile_height - 4)
                pygame.draw.rect(self.screen, (160, 160, 160), tile_rect)
                pygame.draw.lines(self.screen, (250, 54, 31), 1, owr_points, 3)

    def DrawPlayer(self):
        player_rect = pygame.Rect(self.player_position_x * self.tile_width, (self.player_position_y * self.tile_height) + 80, self.tile_width, self.tile_height)
        pygame.draw.rect(self.screen, (153, 51, 255), player_rect)
        mouse_direction = self.FindMouseDirection()

        if mouse_direction == "up":
            gun_rect = pygame.Rect((self.player_position_x * self.tile_width) + 15, (self.player_position_y * self.tile_height) + 70, 10, 30)
        elif mouse_direction == "down":
            gun_rect = pygame.Rect((self.player_position_x * self.tile_width) + 15, (self.player_position_y * self.tile_height) + 100, 10, 30)
        elif mouse_direction == "left":
            gun_rect = pygame.Rect((self.player_position_x * self.tile_width) - 10, (self.player_position_y * self.tile_height) + 95, 30, 10)
        elif mouse_direction == "right":
            gun_rect = pygame.Rect((self.player_position_x * self.tile_width) + 20, (self.player_position_y * self.tile_height) + 95, 30, 10)
        pygame.draw.rect(self.screen, (123, 21, 225), gun_rect)

    def MovePlayer(self, direction):
        if self.CheckCollide(direction):
            if direction == "up":
                self.player_position_y -= 1
            elif direction == "left":
                self.player_position_x -= 1
            elif direction == "down":
                self.player_position_y += 1
            elif direction == "right":
                self.player_position_x += 1
    
    def CheckCollide(self, direction):
        test_x = self.player_position_x
        test_y = self.player_position_y
        if direction == "up":
            test_y -= 1
        elif direction == "left":
            test_x -= 1
        elif direction == "down":
            test_y += 1
        elif direction == "right":
            test_x += 1
        
        if test_x == self.portal_blue[0] and test_y == self.portal_blue[1] and self.portal_blue[2] == self.InvertDir(direction):
            if self.portal_orange[0] != 0 or self.portal_orange[1] != 0 or self.portal_orange[2] != 0:
                self.TpToOrange()
                return False
        elif test_x == self.portal_orange[0] and test_y == self.portal_orange[1] and self.portal_orange[2] == self.InvertDir(direction):
            if self.portal_blue[0] != 0 or self.portal_blue[1] != 0 or self.portal_blue[2] != 0:
                self.TpToBlue()
                return False
        elif not self.CollideForOneWay(direction, self.level[test_x + (test_y * self.lvl_width)]):
            return False
        elif self.level[test_x + (test_y * self.lvl_width)] == "mur":
            return False
        elif self.level[test_x + (test_y * self.lvl_width)] == "lav":
            return False
        elif self.level[test_x + (test_y * self.lvl_width)] == "mlu":
            return False
        elif self.level[test_x + (test_y * self.lvl_width)] == "mld":
            return False
        else:
            return True

    def InvertDir(self, direction):
        if direction == "up":
            return "down"
        elif direction == "down":
            return "up"
        elif direction == "left":
            return "right"
        elif direction == "right":
            return "left"
    
    def CheckIfPortaillable(self, x, y, direction):
        level_index = (y * self.lvl_width) + x
        if direction == "up":
            level_index -= self.lvl_width
        if direction == "down":
            level_index += self.lvl_width
        if direction == "left":
            level_index -= 1
        if direction == "right":
            level_index += 1
        if self.level[level_index] == "air" or level_index == "fin":
            return True
        else:
            return False

    def SendPortal(self, portal_color):

        mouse_direction = self.FindMouseDirection()
        x, y, portal_direction = self.SearchWall(mouse_direction)
        if not self.CheckIfPortaillable(x, y, portal_direction):
            pass

        elif x == 0 and y == 0 and portal_direction == 0:
            pass

        elif portal_color == "orange":
            if self.portal_blue[0] != x or self.portal_blue[1] != y or self.portal_blue[2] != portal_direction:
                self.portal_orange = [x, y, portal_direction]
        elif portal_color == "blue":
            if self.portal_orange[0] != x or self.portal_orange[1] != y or self.portal_orange[2] != portal_direction:
                self.portal_blue = [x, y, portal_direction]

    def SearchWall(self, direction):
        test_x = self.player_position_x
        test_y = self.player_position_y
        while self.level[test_x + test_y * self.lvl_width] == "air" or self.level[test_x + test_y * self.lvl_width] == "lav" or self.level[test_x + test_y * self.lvl_width] == "ply" or self.level[test_x + test_y * self.lvl_width] == "fin"or self.level[test_x + test_y * self.lvl_width] == "mlu" or self.level[test_x + test_y * self.lvl_width] == "mld" or self.level[test_x + test_y * self.lvl_width] == "owu" or self.level[test_x + test_y * self.lvl_width] == "owd" or self.level[test_x + test_y * self.lvl_width] == "owr" or self.level[test_x + test_y * self.lvl_width] == "owl":
            if direction == "up":
                test_y -= 1
            if direction == "down":
                test_y += 1
            if direction == "left":
                test_x -= 1
            if direction == "right":
                test_x += 1
            if self.level[test_x + test_y * self.lvl_width] == "res":
                return 0, 0, 0
            if not self.CollideForOneWay(direction, self.level[test_x + test_y * self.lvl_width]):
                return 0, 0, 0
            if self.level[test_x + test_y * self.lvl_width] == "mld":
                if direction == "up":
                    direction = "left"
                elif direction == "down":
                    direction = "right"
                elif direction == "left":
                    direction = "up"
                elif direction == "right":
                    direction = "down"
            if self.level[test_x + test_y * self.lvl_width] == "mlu":
                if direction == "up":
                    direction = "right"
                elif direction == "down":
                    direction = "left"
                elif direction == "left":
                    direction = "down"
                elif direction == "right":
                    direction = "up"

        portal_direction = self.InvertDir(direction)

        return test_x, test_y, portal_direction

    def FindMouseDirection(self):
        player_middle_x = (self.player_position_x * self.tile_width) + 20
        player_middle_y = (self.player_position_y * self.tile_height) + 100
        mouse_pos_x, mouse_pos_y = pygame.mouse.get_pos()

        diff_x = player_middle_x - mouse_pos_x
        diff_y = player_middle_y - mouse_pos_y

        diff_x_abs = abs(diff_x)
        diff_y_abs = abs(diff_y)

        if diff_x >= 0 and diff_x_abs >= diff_y_abs:
            return "left"
        elif diff_x <= 0 and diff_x_abs >= diff_y_abs:
            return "right"
        elif diff_y >= 0 and diff_y_abs >= diff_x_abs:
            return "up"
        elif diff_y <= 0 and diff_y_abs >= diff_x_abs:
            return "down"
        
    def DrawPortals(self):
        if self.portal_blue[2] == "left":
            blue_portal_rect = pygame.Rect((self.portal_blue[0] * self.tile_width) -5 , (self.portal_blue[1] * self.tile_height) + 80, 5, 40)
        elif self.portal_blue[2] == "right":
            blue_portal_rect = pygame.Rect((self.portal_blue[0] * self.tile_width) +40 , (self.portal_blue[1] * self.tile_height) + 80, 5, 40)
        elif self.portal_blue[2] == "up":
            blue_portal_rect = pygame.Rect((self.portal_blue[0] * self.tile_width), (self.portal_blue[1] * self.tile_height) + 75, 40, 5)
        elif self.portal_blue[2] == "down":
            blue_portal_rect = pygame.Rect((self.portal_blue[0] * self.tile_width), (self.portal_blue[1] * self.tile_height) + 120, 40, 5)
        if self.portal_orange[2] == "left":
            orange_portal_rect = pygame.Rect((self.portal_orange[0] * self.tile_width) -5 , (self.portal_orange[1] * self.tile_height) + 80, 5, 40)
        elif self.portal_orange[2] == "right":
            orange_portal_rect = pygame.Rect((self.portal_orange[0] * self.tile_width) +40 , (self.portal_orange[1] * self.tile_height) + 80, 5, 40)
        elif self.portal_orange[2] == "up":
            orange_portal_rect = pygame.Rect((self.portal_orange[0] * self.tile_width), (self.portal_orange[1] * self.tile_height) + 75, 40, 5)
        elif self.portal_orange[2] == "down":
            orange_portal_rect = pygame.Rect((self.portal_orange[0] * self.tile_width), (self.portal_orange[1] * self.tile_height) + 120, 40, 5)
        
        if self.portal_blue[2] != 0:
            pygame.draw.rect(self.screen, (32, 111, 247), blue_portal_rect)

        if self.portal_orange[2] != 0:
            pygame.draw.rect(self.screen, (235, 132, 29), orange_portal_rect)

    def TpToOrange(self):
        self.player_position_x = self.portal_orange[0]
        self.player_position_y = self.portal_orange[1]
        if self.portal_orange[2] == "up":
            self.player_position_y -= 1
        if self.portal_orange[2] == "down":
            self.player_position_y += 1
        if self.portal_orange[2] == "left":
            self.player_position_x -= 1
        if self.portal_orange[2] == "right":
            self.player_position_x += 1

    def TpToBlue(self):
        self.player_position_x = self.portal_blue[0]
        self.player_position_y = self.portal_blue[1]
        if self.portal_blue[2] == "up":
            self.player_position_y -= 1
        if self.portal_blue[2] == "down":
            self.player_position_y += 1
        if self.portal_blue[2] == "left":
            self.player_position_x -= 1
        if self.portal_blue[2] == "right":
            self.player_position_x += 1
        
    def ResetPortal(self):
        self.portal_orange = [0, 0, 0]
        self.portal_blue = [0, 0, 0]
    
    def ResetSeconde(self):
        self.seconde = 0

    def SetTime(self, default_time):
        minute = default_time // 60
        seconde = default_time % 60
        return "Time: " + str(minute) + " m " + str(seconde) + " s"

    def CollideForOneWay(self, direction, index):
        if direction == "up" and index == "owd":
            return False
        elif direction == "left"and index == "owr":
            return False
        elif direction == "down"and index == "owu":
            return False
        elif direction == "right"and index == "owl":
            return False
        return True

    def PosBlock(self):
        mouse_pos_x, mouse_pos_y = pygame.mouse.get_pos()
        level_rect = pygame.Rect(40, 120, (40*28), (40*16))
        
        if level_rect.collidepoint(mouse_pos_x, mouse_pos_y):
            if self.selected == "ply":
                if "ply" in self.level:
                    self.level[self.level.index("ply")] = "air"
            tile_x = mouse_pos_x // 40
            tile_y = (mouse_pos_y // 40) - 2
            self.level[tile_x + (tile_y * self.lvl_width)] = self.selected

    def DelBlock(self):
        mouse_pos_x, mouse_pos_y = pygame.mouse.get_pos()
        level_rect = pygame.Rect(40, 120, (40*28), (40*16))
        if level_rect.collidepoint(mouse_pos_x, mouse_pos_y):
            tile_x = mouse_pos_x // 40
            tile_y = (mouse_pos_y // 40) - 2
            self.level[tile_x + (tile_y * self.lvl_width)] = "air"

    def SetPlayerPos(self):
        if "ply" in self.level:
            index = self.level.index("ply")
            self.player_position_x = index % self.lvl_width
            self.player_position_y = index // self.lvl_width

    def DrawSelectedTile(self):
        mouse_pos_x, mouse_pos_y = pygame.mouse.get_pos()
        level_rect = pygame.Rect(40, 120, (40*28), (40*16))
        print("1")
        
        if level_rect.collidepoint(mouse_pos_x, mouse_pos_y):
            tile_x = mouse_pos_x // 40
            tile_y = (mouse_pos_y // 40)
            rect1 = (tile_x * 40, tile_y * 40, 40, 2)
            rect2 = (tile_x * 40, tile_y * 40, 2, 40)
            rect3 = (tile_x * 40, (tile_y * 40) + 38, 40, 2)
            rect4 = ((tile_x * 40) + 38, tile_y * 40, 2, 40)
            pygame.draw.rect(self.screen, (20, 20, 20), rect1)
            pygame.draw.rect(self.screen, (20, 20, 20), rect2)
            pygame.draw.rect(self.screen, (20, 20, 20), rect3)
            pygame.draw.rect(self.screen, (20, 20, 20), rect4)
            print("2")