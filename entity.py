__author__ = 'Jacob Chaves'
"""
"""

from kivy.uix.widget import Widget
from kivy.uix.image import Image

class Entity(Widget):
    def __init__(self, imgName):
        image = Image(source=imgName)

    def move(self):
        pass