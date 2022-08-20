#import pygame
import pygame

#class boton
class Button():
    def __init__(self, x, y, width, heigth, color_background, color_over, text, color_text, text_size):
        #set fonction
        self.x = x
        self.y = y
        self.width = width
        self.height = heigth
        self.rect = (x, y, width, heigth)
        self.color_background = color_background
        self.color_over = color_over
        self.text = text
        self.color_text = color_text
        self.text_size = text_size

        #set font
        self.text_font = pygame.font.Font("model/square_font.ttf", self.text_size)

    def DrawButton (self, screen):
        #set le text
        text = self.text_font.render(self.text , True, (0, 0, 0))
        text_rect = text.get_rect(center=(self.x + (self.width / 2), self.y + (self.height / 2)))

        #draw text
        pygame.draw.rect(screen, self.color_background, self.rect)
        screen.blit(text, text_rect)