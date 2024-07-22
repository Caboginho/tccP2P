from kivy.uix.screenmanager import Screen
from kivymd.app import MDApp

class SellerScreen(Screen):
    def add_product(self):
        name = self.ids.name_field.text
        description = self.ids.description_field.text
        price = float(self.ids.price_field.text)
        seller_id = 1  # Aqui você deve obter o ID do vendedor logado
        app = MDApp.get_running_app()
        app.db.insert_product(name, description, price, seller_id)
        self.ids.message.text = "Product added successfully!"

    def update_product(self):
        name = self.ids.name_field.text
        description = self.ids.description_field.text
        price = float(self.ids.price_field.text)
        seller_id = 1  # Aqui você deve obter o ID do vendedor logado
        app = MDApp.get_running_app()
        app.db.update_product(name, description, price, seller_id)
        self.ids.message.text = "Product updated successfully!"

    def delete_product(self):
        name = self.ids.name_field.text
        app = MDApp.get_running_app()
        app.db.delete_product(name)
        self.ids.message.text = "Product deleted successfully!"
