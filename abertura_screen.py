from kivy.uix.screenmanager import Screen
from kivymd.app import MDApp
from time import sleep

class AberturaScreen(Screen):
    def play(self):
        sleep(3)
        app = MDApp.get_running_app()
        self.manager.current = "login"