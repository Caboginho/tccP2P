from kivy.uix.screenmanager import Screen
from kivymd.app import MDApp
from datetime import datetime

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
        product = app.db.get_product(name)
        if product:
            buyer_id = 1  # Aqui você deve obter o ID do comprador logado
            date = datetime.now().strftime('%Y-%m-%d %H:%M:%S')
            app.db.insert_purchase(product[0], buyer_id, date)
            self.ids.message.text = "Product purchased successfully!"
        else:
            self.ids.message.text = "Product not found!"

    def reserve_product(self):
        name = self.ids.name_field.text
        app = MDApp.get_running_app()
        product = app.db.get_product(name)
        if product:
            reserver_id = 1  # Aqui você deve obter o ID do usuário logado
            date = datetime.now().strftime('%Y-%m-%d %H:%M:%S')
            app.db.insert_reservation(product[0], reserver_id, date)
            self.ids.message.text = "Product reserved successfully!"
        else:
            self.ids.message.text = "Product not found!"

    def rent_product(self):
        name = self.ids.name_field.text
        app = MDApp.get_running_app()
        product = app.db.get_product(name)
        if product:
            renter_id = 1  # Aqui você deve obter o ID do usuário logado
            date = datetime.now().strftime('%Y-%m-%d %H:%M:%S')
            app.db.insert_rental(product[0], renter_id, date)
            self.ids.message.text = "Product rented successfully!"
        else:
            self.ids.message.text = "Product not found!"
