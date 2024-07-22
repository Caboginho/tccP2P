"""Estrutura do Projeto
main.py: Inicializa a aplicação e define as telas.
login_screen.py: Gerencia o login e a autenticação.
home_screen.py: Tela principal após o login.
product_screen.py: Gerencia os produtos (adicionar, atualizar, deletar, buscar).
user_screen.py: Gerencia os usuários (clientes e vendedores).
database.py: Gerencia a conexão e operações do banco de dados SQLite.
google_sheets.py: Sincroniza dados com o Google Sheets."""

from kivy.lang import Builder
from kivymd.app import MDApp
from kivy.uix.screenmanager import ScreenManager
from database import Database
from login_screen import LoginScreen
from register_screen import RegisterScreen
from product_screen import ProductScreen
from client_screen import ClientScreen
from seller_screen import SellerScreen
from transfer_screen import TransferScreen
from payment_screen import PaymentScreen

class MainApp(MDApp):
    def build(self):
        self.db = Database()
        self.load_all_kv_files()

        sm = ScreenManager()
        sm.add_widget(LoginScreen(name='login'))
        sm.add_widget(RegisterScreen(name='register'))
        sm.add_widget(ProductScreen(name='product'))
        sm.add_widget(ClientScreen(name='client'))
        sm.add_widget(SellerScreen(name='seller'))
        sm.add_widget(TransferScreen(name='transfer'))
        sm.add_widget(PaymentScreen(name='payment'))
        
        return sm

    def load_all_kv_files(self):
        Builder.load_file('login_screen.kv')
        Builder.load_file('register_screen.kv')
        Builder.load_file('product_screen.kv')
        Builder.load_file('client_screen.kv')
        Builder.load_file('seller_screen.kv')
        Builder.load_file('transfer_screen.kv')
        Builder.load_file('payment_screen.kv')

if __name__ == '__main__':
    MainApp().run()




