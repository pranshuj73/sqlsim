import os

from .database import get_database_connection, close_database_connection
from utils.logging import logger

DB_PATH = os.path.join("data", "database.db")


def fetch_customers(count=10, all=False) -> list | None:
    """
    Fetch N customers from the database.
    Parameters: count: int, all: bool
    count -> Number of customers to fetch (default: 10)
    all -> Fetch all customers if True, else fetch `count` customers
    """

    try:
        conn = get_database_connection()
        if not conn:
            return None
        cursor = conn.cursor()

        cursor.execute("SELECT * FROM customers")
        customers = []
        if all:
            customers = cursor.fetchall()
        else:
            customers = cursor.fetchmany(count)

        close_database_connection(conn)

        return customers

    except Exception as e:
        logger.error(f"Error fetching customers: {e}")
        return None


def fetch_products(count=10, all=False) -> list | None:
    """
    Fetch N products from the database.
    Parameters: count: int, all: bool
    count -> Number of products to fetch (default: 10)
    all -> Fetch all products if True, else fetch `count` products
    """

    try:
        conn = get_database_connection()
        if not conn:
            return None
        cursor = conn.cursor()

        cursor.execute("SELECT * FROM products")
        products = []
        if all:
            products = cursor.fetchall()
        else:
            products = cursor.fetchmany(count)

        close_database_connection(conn)

        return products

    except Exception as e:
        logger.error(f"Error fetching products: {e}")
        return None


def fetch_orders(count=10, all=False) -> list | None:
    """
    Fetch N orders from the database.
    Parameters: count: int, all: bool
    count -> Number of orders to fetch (default: 10)
    all -> Fetch all orders if True, else fetch `count` orders
    """

    try:
        conn = get_database_connection()
        if not conn:
            return None
        cursor = conn.cursor()

        cursor.execute("SELECT * FROM orders")
        orders = []
        if all:
            orders = cursor.fetchall()
        else:
            orders = cursor.fetchmany(count)

        close_database_connection(conn)

        return orders

    except Exception as e:
        logger.error(f"Error fetching orders: {e}")
        return None
