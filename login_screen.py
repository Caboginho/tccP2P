from kivy.uix.screenmanager import Screen
from kivymd.app import MDApp

class LoginScreen(Screen):
    def do_login(self):
        email = self.ids.email_field.text
        password = self.ids.password_field.text
        app = MDApp.get_running_app()
        if app.db.get_user(email, password):
            self.do_move('client')
        else:
            self.do_move('register')
    def do_move(self, screen):
        self.manager.current = screen