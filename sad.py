from smiley import Smiley
#from blinkable import Blinkable
import time

class Sad(Smiley):
    def __init__(self):
        super().__init__()

        self.draw_mouth()
        self.draw_eyes()

    def draw_mouth(self):
        """
        Draws the mouth feature on a smiley
        """
        mouth = [49, 54, 42, 43, 44, 45]
        for pixel in mouth:
            self.pixels[pixel] = self.BLANK

    def draw_eyes(self, wide_open=True):
        """
        Draws open or closed eyes on a smiley
        :param wide_open: Render eyes wide open or shut
        """
        eyes = [10, 13, 18, 21]
        for pixel in eyes:
            if wide_open:
                eyes_color = self.BLANK
            else:
                eyes_color = self.complexion()
            self.pixels[pixel] = eyes_color

    def blink(self, delay=0.2):
        """
       Blinks the smiley's eyes twice

        :param delay: Delay between blinks (in seconds)
        """
        wide_open = True
        for times in range(4):
            if (wide_open):
                wide_open = False
            else:
                wide_open = True
            self.draw_eyes(wide_open)
            self.show()
            time.sleep(delay)
