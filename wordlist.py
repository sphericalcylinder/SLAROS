import os
import pygame.font as ft

ft.init()

class Sentence:


    def __init__(self, text: str, y: int, usrinput: bool, colors: tuple):
        self.COORDS = (20, y)
        self.txt = text
        self.font = ft.Font(os.environ['SLAROSDIR']+'/andalemono.ttf', 12)
        self.y = y
        self.usrinput = usrinput
        self.colors = colors

    def loadsentence(self):
        if self.usrinput == True:
            return [self.font.render(f"JSH $ {self.txt}", True, self.colors[1]), [20, self.y]]
        else:
            return [self.font.render(self.txt, True, self.colors[1]), [20, self.y]]

    def updatey(self, diff: int):
        self.y -= diff * 25