#import pygame
import pygame

#class boton
class Button():
    def __init__(self, x, y, width, heigth, color_background, color_over, text, text_color, text_size):
        #set fonction
        self.x = x
        self.y = y
        self.width = width
        self.height = heigth
        self.rect = pygame.Rect(x, y, width, heigth)
        self.color_background = color_background
        self.color_over = color_over
        self.text = text
        self.text_color = text_color
        self.text_size = text_size

        #set font
        self.text_font = pygame.font.Font("model/square_font.ttf", text_size)

    def DrawButton (self, screen):
        #set le text
        text = self.text_font.render(self.text , True, self.text_color)
        text_rect = text.get_rect(center=(self.x + (self.width / 2), self.y + (self.height / 2)))

        #get mouse pod
        mouse_pos = pygame.mouse.get_pos()

        #draw text
        if self.rect.collidepoint(mouse_pos):
            pygame.draw.rect(screen, self.color_over, self.rect)
        else:
            pygame.draw.rect(screen, self.color_background, self.rect)
        screen.blit(text, text_rect)

    def IsPressed (self):
        #get mouse pod
        mouse_pos = pygame.mouse.get_pos()
        if self.rect.collidepoint(mouse_pos):
            return True
        else:
            return False
    
class ButtonEditor():
    def __init__(self, x, y, width, heigth, block):
        #set fonction
        self.x = x
        self.y = y
        self.tile_width = width
        self.tile_height = heigth
        self.rect = pygame.Rect(x, y, width, heigth)
        self.block = block

    def DrawButton (self, screen):
        self.screen = screen
        tile_x = self.x
        tile_y = self.y
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
        if self.block == "mur":
            pygame.draw.rect(self.screen, (100, 100, 100), tile_rect)
        
        if self.block == "upw":
            pygame.draw.rect(self.screen, (40, 40, 40), tile_rect)

        elif self.block == "air":
            pygame.draw.rect(self.screen, (180, 180, 180), tile_rect)
            tile_rect = pygame.Rect(tile_x + 2, tile_y + 2, self.tile_width - 4, self.tile_height - 4)
            pygame.draw.rect(self.screen, (220, 220, 220), tile_rect)

        elif self.block == "fin":
            pygame.draw.rect(self.screen, (180, 180, 180), tile_rect)
            tile_rect = pygame.Rect(tile_x + 2, tile_y + 2, self.tile_width - 4, self.tile_height - 4)
            pygame.draw.rect(self.screen, (255, 195, 0), tile_rect)

        elif self.block == "lav":
            pygame.draw.rect(self.screen, (255, 77, 0), tile_rect)

        elif self.block == "res":
            pygame.draw.rect(self.screen, (73, 163, 194), tile_rect)
            tile_rect = pygame.Rect(tile_x + 2, tile_y + 2, self.tile_width - 4, self.tile_height - 4)
            pygame.draw.rect(self.screen, (95, 191, 224), tile_rect)

        elif self.block == "mlu":
            pygame.draw.rect(self.screen, (180, 180, 180), tile_rect)
            tile_rect = pygame.Rect(tile_x + 2, tile_y + 2, self.tile_width - 4, self.tile_height - 4)
            pygame.draw.rect(self.screen, (220, 220, 220), tile_rect)
            pygame.draw.lines(self.screen, (0, 0, 0), 1, mlu_points, 3)
            pygame.draw.line(self.screen, (0, 0, 0), (tile_x , tile_y + 39), (tile_x + 39, tile_y), 2)

        elif self.block == "mld":
            pygame.draw.rect(self.screen, (180, 180, 180), tile_rect)
            tile_rect = pygame.Rect(tile_x + 2, tile_y + 2, self.tile_width - 4, self.tile_height - 4)
            pygame.draw.rect(self.screen, (220, 220, 220), tile_rect)
            pygame.draw.lines(self.screen, (0, 0, 0), 1, mld_points, 3)
            pygame.draw.line(self.screen, (0, 0, 0), (tile_x, tile_y), (tile_x + 39, tile_y + 39), 2)
            
        elif self.block == "owu":
            pygame.draw.rect(self.screen, (180, 180, 180), tile_rect)
            tile_rect = pygame.Rect(tile_x + 2, tile_y + 2, self.tile_width - 4, self.tile_height - 4)
            pygame.draw.rect(self.screen, (200, 200, 200), tile_rect)
            tile_rect = pygame.Rect(tile_x + 2, tile_y + 2, self.tile_width - 4, self.tile_height - 34)
            pygame.draw.rect(self.screen, (160, 160, 160), tile_rect)
            pygame.draw.lines(self.screen, (250, 54, 31), 1, owu_points, 3)

        elif self.block == "owd":
            pygame.draw.rect(self.screen, (180, 180, 180), tile_rect)
            tile_rect = pygame.Rect(tile_x + 2, tile_y + 2, self.tile_width - 4, self.tile_height - 4)
            pygame.draw.rect(self.screen, (200, 200, 200), tile_rect)
            tile_rect = pygame.Rect(tile_x + 2, tile_y + 32, self.tile_width - 4, self.tile_height - 34)
            pygame.draw.rect(self.screen, (160, 160, 160), tile_rect)
            pygame.draw.lines(self.screen, (250, 54, 31), 1, owd_points, 3)

        elif self.block == "owl":
            pygame.draw.rect(self.screen, (180, 180, 180), tile_rect)
            tile_rect = pygame.Rect(tile_x + 2, tile_y + 2, self.tile_width - 4, self.tile_height - 4)
            pygame.draw.rect(self.screen, (200, 200, 200), tile_rect)
            tile_rect = pygame.Rect(tile_x + 2, tile_y + 2, self.tile_width - 34, self.tile_height - 4)
            pygame.draw.rect(self.screen, (160, 160, 160), tile_rect)
            pygame.draw.lines(self.screen, (250, 54, 31), 1, owl_points, 3)

        elif self.block == "owr":
            pygame.draw.rect(self.screen, (180, 180, 180), tile_rect)
            tile_rect = pygame.Rect(tile_x + 2, tile_y + 2, self.tile_width - 4, self.tile_height - 4)
            pygame.draw.rect(self.screen, (200, 200, 200), tile_rect)
            tile_rect = pygame.Rect(tile_x + 32, tile_y + 2, self.tile_width - 34, self.tile_height - 4)
            pygame.draw.rect(self.screen, (160, 160, 160), tile_rect)
            pygame.draw.lines(self.screen, (250, 54, 31), 1, owr_points, 3)

        elif self.block == "ply":
            pygame.draw.rect(self.screen, (153, 51, 255), tile_rect)

            gun_rect = pygame.Rect(self.x - 10, self.y + 95, 30, 10)

            pygame.draw.rect(self.screen, (123, 21, 225), gun_rect)

    def IsPressed (self):
        #get mouse pod
        mouse_pos = pygame.mouse.get_pos()
        if self.rect.collidepoint(mouse_pos):
            return True
        else:
            return False