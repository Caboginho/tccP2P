from kivy.uix.screenmanager import Screen
from kivymd.uix.button import MDRaisedButton
from kivymd.uix.textfield import MDTextField
from kivymd.uix.label import MDLabel
from kivymd.uix.boxlayout import MDBoxLayout

class LoginScreen(Screen):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        
        self.layout = MDBoxLayout(orientation='vertical', padding=40, spacing=20)
        self.add_widget(self.layout)

        self.email = MDTextField(
            hint_text="Email",
            pos_hint={"center_x": 0.5, "center_y": 0.6},
            size_hint_x=0.8
        )
        self.layout.add_widget(self.email)

        self.password = MDTextField(
            hint_text="Password",
            password=True,
            pos_hint={"center_x": 0.5, "center_y": 0.5},
            size_hint_x=0.8
        )
        self.layout.add_widget(self.password)

        self.login_button = MDRaisedButton(
            text="Login",
            pos_hint={"center_x": 0.5, "center_y": 0.4},
            on_release=self.do_login
        )
        self.layout.add_widget(self.login_button)

        self.message = MDLabel(
            text="",
            halign="center",
            theme_text_color="Error"
        )
        self.layout.add_widget(self.message)

    def do_login(self, instance):
        email = self.email.text
        password = self.password.text
        if email and password:
            self.manager.current = 'home'
        else:
            self.message.text = "Please enter both email and password"
