import sqlite3
import os

from utils.logging import logger

DB_PATH = os.path.join("data", "database.db")


def fetch_customers(count=10, all=False) -> list | None:
    """
    Fetch N customers from the database.
    """

    try:
        conn = sqlite3.connect(DB_PATH)
        cursor = conn.cursor()

        cursor.execute("SELECT * FROM customers")
        customers = []
        if all:
            customers = cursor.fetchall()
        else:
            customers = cursor.fetchmany(count)

        conn.close()

        return customers

    except sqlite3.Error as e:
        logger.error(f"Error fetching customers: {e}")
        return None


def fetch_products(count=10, all=False) -> list | None:
    """
    Fetch N products from the database.
    """

    try:
        conn = sqlite3.connect(DB_PATH)
        cursor = conn.cursor()

        cursor.execute("SELECT * FROM products")
        products = []
        if all:
            products = cursor.fetchall()
        else:
            products = cursor.fetchmany(count)

        conn.close()

        return products

    except sqlite3.Error as e:
        logger.error(f"Error fetching products: {e}")
        return None
