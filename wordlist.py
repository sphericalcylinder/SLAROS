import os
import pygame.font as ft

ft.init()

class Sentence:


    def __init__(self, text: str, y: int, usrinput: bool):
        self.COORDS = (20, y)
        self.txt = text
        self.font = ft.Font(os.environ['SLAROSDIR']+'/andalemono.ttf', 12)
        self.y = y
        self.usrinput = usrinput

    def loadsentence(self):
        if self.usrinput == True:
            return [self.font.render(f"JSH $ {self.txt}", True, (0, 0, 0)), [20, self.y]]
        else:
            return [self.font.render(self.txt, True, (0, 0, 0)), [20, self.y]]

    def updatey(self, diff: int):
        self.y -= diff * 25