import pygame.font as ft

ft.init()

class Sentence:


    def __init__(self, text, y):
        self.COORDS = (20, y)
        self.txt = text
        self.font = ft.Font('assets/andalemono.ttf', 12)
        self.y = y

    def loadsentence(self):
        return [self.font.render(self.txt, True, (0, 0, 0)), [20, self.y]]