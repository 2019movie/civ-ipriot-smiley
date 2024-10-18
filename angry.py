from smiley import Smiley
from blinkable import Blinkable
import time

class Angry(Smiley, Blinkable):
    def __init__(self):
        super().__init__(complexion=self.RED)

        self.draw_mouth()
        self.draw_eyes()

    def draw_mouth(self):
        """
        Draws the mouth feature on a smiley
        """
        mouth = [36, 35, 42, 43, 44, 45]
        for pixel in mouth:
            self.pixels[pixel] = self.BLANK

    def draw_eyes(self, wide_open=True):
        """
        Draws open or closed eyes on a smiley
        :param wide_open: Render eyes wide open or shut
        """
        eyes = [0, 7, 9, 14, 18, 21]
        for pixel in eyes:
            if wide_open:
                eyes_color = self.BLANK
            else:
                eyes_color = self.complexion()
            self.pixels[pixel] = eyes_color

    def blink(self, delay=0.1):
        """
       Blinks the smiley's eyes twice

        :param delay: Delay between blinks (in seconds)
        """
        wide_open = True
        for times in range(8):
            if (wide_open):
                wide_open = False
            else:
                wide_open = True
            self.draw_eyes(wide_open)
            self.show()
            time.sleep(delay)