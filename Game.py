__author__ = 'Jacob Chaves'
"""
This is the main file for project 1.  This is simply
an intro to kivy and getting used to its unique
take on language.
"""

from kivy.app import App
from kivy.core.window import Window
from kivy.uix.widget import Widget
from kivy.uix.image import Image
from kivy.clock import Clock

class GameWindow(Widget):
    def update(self):
        pass

class Game(App):
    def build(self):
        gameWindow = GameWindow()
        #Clock.schedule_interval(gameWindow.update, 1.0/60.0)
        return gameWindow


if __name__ == '__main__':
    Game().run()