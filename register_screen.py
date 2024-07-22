from kivy.uix.screenmanager import Screen
from kivymd.uix.button import MDRaisedButton
from kivymd.uix.textfield import MDTextField
from kivymd.uix.boxlayout import MDBoxLayout
from kivymd.uix.label import MDLabel
from kivymd.app import MDApp

class RegisterScreen(Screen):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        
        self.layout = MDBoxLayout(orientation='vertical', padding=40, spacing=20)
        self.add_widget(self.layout)

        self.name = MDTextField(
            hint_text="Name",
            pos_hint={"center_x": 0.5, "center_y": 0.8},
            size_hint_x=0.8
        )
        self.layout.add_widget(self.name)

        self.email = MDTextField(
            hint_text="Email",
            pos_hint={"center_x": 0.5, "center_y": 0.7},
            size_hint_x=0.8
        )
        self.layout.add_widget(self.email)

        self.password = MDTextField(
            hint_text="Password",
            password=True,
            pos_hint={"center_x": 0.5, "center_y": 0.6},
            size_hint_x=0.8
        )
        self.layout.add_widget(self.password)

        self.user_type = MDTextField(
            hint_text="User Type (customer/seller)",
            pos_hint={"center_x": 0.5, "center_y": 0.5},
            size_hint_x=0.8
        )
        self.layout.add_widget(self.user_type)

        self.register_button = MDRaisedButton(
            text="Register",
            pos_hint={"center_x": 0.5, "center_y": 0.4},
            on_release=self.do_register
        )
        self.layout.add_widget(self.register_button)

        self.message = MDLabel(
            text="",
            halign="center",
            theme_text_color="Error"
        )
        self.layout.add_widget(self.message)

    def do_register(self, instance):
        name = self.name.text
        email = self.email.text
        password = self.password.text
        user_type = self.user_type.text
        app = MDApp.get_running_app()
        if name and email and password and user_type:
            app.db.insert_user(name, email, password, user_type)
            self.manager.current = 'login'
        else:
            self.message.text = "Please fill in all fields"
