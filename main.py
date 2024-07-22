"""Estrutura do Projeto
main.py: Inicializa a aplicação e define as telas.
login_screen.py: Gerencia o login e a autenticação.
home_screen.py: Tela principal após o login.
product_screen.py: Gerencia os produtos (adicionar, atualizar, deletar, buscar).
user_screen.py: Gerencia os usuários (clientes e vendedores).
database.py: Gerencia a conexão e operações do banco de dados SQLite.
google_sheets.py: Sincroniza dados com o Google Sheets."""

from kivy.lang import Builder
from kivy.core.window import Window
from kivy.uix.screenmanager import ScreenManager, Screen
from kivymd.app import MDApp
from login_screen import LoginScreen
from home_screen import HomeScreen
from product_screen import ProductScreen
from user_screen import UserScreen
from register_screen import RegisterScreen
from database import Database

Window.size = (360, 640)  # Define o tamanho da janela

class MainApp(MDApp):
    def build(self):
        self.title = "iFood Clone"
        self.db = Database()  # Inicializa o banco de dados

        sm = ScreenManager()
        sm.add_widget(LoginScreen(name='login'))
        sm.add_widget(RegisterScreen(name='register'))
        sm.add_widget(HomeScreen(name='home'))
        sm.add_widget(ProductScreen(name='product'))
        sm.add_widget(UserScreen(name='user'))
        return sm

if __name__ == '__main__':
    MainApp().run()

