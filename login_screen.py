from kivy.uix.screenmanager import Screen
from kivymd.app import MDApp

class LoginScreen(Screen):
    def do_login(self):
        email = self.ids.email_field.text
        password = self.ids.password_field.text
        app = MDApp.get_running_app()
        user = app.db.get_user(email, password)
        if user:
            self.manager.current = 'product'
        else:
            self.manager.current = 'register'
