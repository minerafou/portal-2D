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
        self.id = id

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