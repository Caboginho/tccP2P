import sqlite3

class Database:
    def __init__(self, db_name="ifood_clone.db"):
        self.connection = sqlite3.connect(db_name)
        self.create_tables()

    def create_tables(self):
        with self.connection:
            self.connection.execute(
                "CREATE TABLE IF NOT EXISTS users (id INTEGER PRIMARY KEY, name TEXT, email TEXT, password TEXT, type TEXT)"
            )
            self.connection.execute(
                "CREATE TABLE IF NOT EXISTS products (id INTEGER PRIMARY KEY, name TEXT, description TEXT, price REAL, seller_id INTEGER)"
            )

    def insert_user(self, name, email, password, user_type):
        with self.connection:
            self.connection.execute(
                "INSERT INTO users (name, email, password, type) VALUES (?, ?, ?, ?)",
                (name, email, password, user_type)
            )

    def insert_product(self, name, description, price, seller_id):
        with self.connection:
            self.connection.execute(
                "INSERT INTO products (name, description, price, seller_id) VALUES (?, ?, ?, ?)",
                (name, description, price, seller_id)
            )

    def check_login(self, email, password):
        with self.connection:
            cursor = self.connection.cursor()
            cursor.execute("SELECT * FROM users WHERE email = ? AND password = ?", (email, password))
            return cursor.fetchone()

    # Adicionar outros métodos conforme necessário
