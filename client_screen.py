from kivy.uix.screenmanager import Screen
from kivymd.app import MDApp

class ClientScreen(Screen):
    def search_product(self):
        name = self.ids.name_field.text
        app = MDApp.get_running_app()
        product = app.db.get_product(name)
        if product:
            self.ids.description_field.text = product[2]
            self.ids.price_field.text = str(product[3])
            self.ids.seller_id_field.text = str(product[4])
            self.ids.message.text = "Product found!"
        else:
            self.ids.message.text = "Product not found!"

    def purchase_product(self):
        name = self.ids.name_field.text
        app = MDApp.get_running_app()
        # Implementar lógica de compra de produto
        self.ids.message.text = "Product purchased successfully!"

    def reserve_product(self):
        name = self.ids.name_field.text
        app = MDApp.get_running_app()
        # Implementar lógica de reserva de produto
        self.ids.message.text = "Product reserved successfully!"

    def rent_product(self):
        name = self.ids.name_field.text
        app = MDApp.get_running_app()
        # Implementar lógica de aluguel de produto
        self.ids.message.text = "Product rented successfully!"
