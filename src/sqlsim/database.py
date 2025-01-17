import sqlite3
import os
import json

from utils.logging import logger

DB_PATH = os.path.join("data", "database.db")


def initialise_database() -> None:
    """
    Initialise the database by creating the necessary tables.
    """

    try:
        conn = sqlite3.connect(DB_PATH)
        cursor = conn.cursor()

        cursor.execute(
            """
            CREATE TABLE customers (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                name TEXT NOT NULL,
                email TEXT NOT NULL UNIQUE,
                acc_created DATE NOT NULL
            );
        """
        )

        cursor.execute(
            """
            CREATE TABLE products (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                name TEXT NOT NULL,
                unit_price REAL NOT NULL
            );
        """
        )

        cursor.execute(
            """
            CREATE TABLE orders (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                product_id INTEGER NOT NULL,
                customer_id INTEGER NOT NULL,
                units_purchased INTEGER NOT NULL,
                purchase_date DATE NOT NULL,
                FOREIGN KEY (product_id) REFERENCES products (id),
                FOREIGN KEY (customer_id) REFERENCES customers (id)
            );
        """
        )

        conn.commit()
        conn.close()

        logger.info("Database initialised successfully.")

    except sqlite3.Error as e:
        logger.error(f"Error initialising the database: {e}")


def get_database_connection() -> sqlite3.Connection | None:
    """
    Get a connection to the database.
    """

    try:
        conn = sqlite3.connect(DB_PATH)
        logger.info("Database connection established.")
        return conn
    except sqlite3.Error as e:
        logger.error(f"Error connecting to the database: {e}")
        return


def close_database_connection(conn) -> None:
    """
    Close the connection to the database.
    """

    if conn:
        conn.close()
        logger.info("Database connection closed.")


def populate_customers_table(filename="customers.json") -> None:
    """
    Populate the customers table with sample data.
    """

    try:
        file_path = os.path.join("data/input", filename)

        conn = get_database_connection()
        if not conn:
            return
        cursor = conn.cursor()

        with open(file_path, "r") as f:
            customers = json.load(f)

            for customer in customers:
                cursor.execute(
                    """
                    INSERT INTO customers (name, email, acc_created)
                    VALUES (?, ?, ?);
                    """,
                    (
                        customer["name"],
                        customer["email"],
                        customer["acc_created"]
                    ),
                )

        conn.commit()
        close_database_connection(conn)

        logger.info("Sample customers data populated successfully.")

    except Exception as e:
        logger.error(f"Error populating sample customers data: {e}")


def populate_products_table(filename="products.json") -> None:
    """
    Populate the products table with sample data.
    """

    try:
        file_path = os.path.join("data/input", filename)

        conn = get_database_connection()
        if not conn:
            return
        cursor = conn.cursor()

        with open(file_path, "r") as f:
            products = json.load(f)

            for product in products:
                cursor.execute(
                    """
                    INSERT INTO products (name, unit_price)
                    VALUES (?, ?);
                    """,
                    (
                        product["name"],
                        product["unit_price"]
                    ),
                )

        conn.commit()
        close_database_connection(conn)

        logger.info("Sample products data populated successfully.")

    except Exception as e:
        logger.error(f"Error populating sample products data: {e}")
