from kivy.uix.screenmanager import Screen
from kivymd.app import MDApp

class RegisterScreen(Screen):
    def register_user(self):
        name = self.ids.name_field.text
        email = self.ids.email_field.text
        password = self.ids.password_field.text
        app = MDApp.get_running_app()
        app.db.insert_user(name, email, password, 'client')
        self.ids.message.text = "User registered successfully!"
