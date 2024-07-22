import sqlite3

class Database:
    def __init__(self):
        self.connection = sqlite3.connect('app.db')
        self.create_tables()

    def create_tables(self):
        with self.connection:
            self.connection.execute('''CREATE TABLE IF NOT EXISTS users (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                name TEXT NOT NULL,
                email TEXT NOT NULL UNIQUE,
                password TEXT NOT NULL,
                user_type TEXT NOT NULL
            )''')

            self.connection.execute('''CREATE TABLE IF NOT EXISTS products (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                name TEXT NOT NULL,
                description TEXT NOT NULL,
                price REAL NOT NULL,
                seller_id INTEGER NOT NULL,
                FOREIGN KEY (seller_id) REFERENCES users(id)
            )''')

            self.connection.execute('''CREATE TABLE IF NOT EXISTS purchases (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                product_id INTEGER NOT NULL,
                buyer_id INTEGER NOT NULL,
                date TEXT NOT NULL,
                FOREIGN KEY (product_id) REFERENCES products(id),
                FOREIGN KEY (buyer_id) REFERENCES users(id)
            )''')

            self.connection.execute('''CREATE TABLE IF NOT EXISTS reservations (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                product_id INTEGER NOT NULL,
                reserver_id INTEGER NOT NULL,
                date TEXT NOT NULL,
                FOREIGN KEY (product_id) REFERENCES products(id),
                FOREIGN KEY (reserver_id) REFERENCES users(id)
            )''')

            self.connection.execute('''CREATE TABLE IF NOT EXISTS rentals (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                product_id INTEGER NOT NULL,
                renter_id INTEGER NOT NULL,
                date TEXT NOT NULL,
                FOREIGN KEY (product_id) REFERENCES products(id),
                FOREIGN KEY (renter_id) REFERENCES users(id)
            )''')

    def insert_user(self, name, email, password, user_type):
        with self.connection:
            self.connection.execute('INSERT INTO users (name, email, password, user_type) VALUES (?, ?, ?, ?)',
                                    (name, email, password, user_type))

    def get_user(self, email, password):
        with self.connection:
            cursor = self.connection.cursor()
            cursor.execute('SELECT * FROM users WHERE email = ? AND password = ?', (email, password))
            return cursor.fetchone()

    def insert_product(self, name, description, price, seller_id):
        with self.connection:
            self.connection.execute('INSERT INTO products (name, description, price, seller_id) VALUES (?, ?, ?, ?)',
                                    (name, description, price, seller_id))

    def get_product(self, name):
        with self.connection:
            cursor = self.connection.cursor()
            cursor.execute('SELECT * FROM products WHERE name = ?', (name,))
            return cursor.fetchone()

    def update_product(self, name, description, price, seller_id):
        with self.connection:
            self.connection.execute('''UPDATE products
                                       SET description = ?, price = ?, seller_id = ?
                                       WHERE name = ?''', (description, price, seller_id, name))

    def delete_product(self, name):
        with self.connection:
            self.connection.execute('DELETE FROM products WHERE name = ?', (name,))

    def insert_purchase(self, product_id, buyer_id, date):
        with self.connection:
            self.connection.execute('INSERT INTO purchases (product_id, buyer_id, date) VALUES (?, ?, ?)',
                                    (product_id, buyer_id, date))

    def insert_reservation(self, product_id, reserver_id, date):
        with self.connection:
            self.connection.execute('INSERT INTO reservations (product_id, reserver_id, date) VALUES (?, ?, ?)',
                                    (product_id, reserver_id, date))

    def insert_rental(self, product_id, renter_id, date):
        with self.connection:
            self.connection.execute('INSERT INTO rentals (product_id, renter_id, date) VALUES (?, ?, ?)',
                                    (product_id, renter_id, date))
