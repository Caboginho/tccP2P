from kivy.uix.screenmanager import Screen
from kivymd.uix.button import MDRaisedButton
from kivymd.uix.textfield import MDTextField

class LoginScreen(Screen):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.add_widget(MDTextField(
            hint_text="Email",
            pos_hint={"center_x": 0.5, "center_y": 0.6},
            size_hint_x=0.8
        ))
        self.add_widget(MDTextField(
            hint_text="Password",
            password=True,
            pos_hint={"center_x": 0.5, "center_y": 0.5},
            size_hint_x=0.8
        ))
        self.add_widget(MDRaisedButton(
            text="Login",
            pos_hint={"center_x": 0.5, "center_y": 0.4},
            on_release=self.do_login
        ))

    def do_login(self, instance):
        # Implementar lógica de login aqui
        self.manager.current = 'home'
