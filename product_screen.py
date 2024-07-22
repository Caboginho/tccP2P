from kivy.uix.screenmanager import Screen
from kivymd.uix.button import MDRaisedButton
from kivymd.uix.textfield import MDTextField
from kivymd.uix.boxlayout import MDBoxLayout

class ProductScreen(Screen):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        
        self.layout = MDBoxLayout(orientation='vertical', padding=40, spacing=20)
        self.add_widget(self.layout)

        self.name = MDTextField(
            hint_text="Product Name",
            pos_hint={"center_x": 0.5, "center_y": 0.7},
            size_hint_x=0.8
        )
        self.layout.add_widget(self.name)

        self.description = MDTextField(
            hint_text="Description",
            pos_hint={"center_x": 0.5, "center_y": 0.6},
            size_hint_x=0.8
        )
        self.layout.add_widget(self.description)

        self.price = MDTextField(
            hint_text="Price",
            pos_hint={"center_x": 0.5, "center_y": 0.5},
            size_hint_x=0.8
        )
        self.layout.add_widget(self.price)

        self.seller_id = MDTextField(
            hint_text="Seller ID",
            pos_hint={"center_x": 0.5, "center_y": 0.4},
            size_hint_x=0.8
        )
        self.layout.add_widget(self.seller_id)

        self.add_button = MDRaisedButton(
            text="Add Product",
            pos_hint={"center_x": 0.5, "center_y": 0.3},
            on_release=self.add_product
        )
        self.layout.add_widget(self.add_button)

    def add_product(self, instance):
        name = self.name.text
        description = self.description.text
        price = float(self.price.text)
        seller_id = int(self.seller_id.text)
        #app = MDApp.get_running_app()
        #app.db.insert_product(name, description, price, seller_id)
