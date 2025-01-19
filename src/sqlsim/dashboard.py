import os
from datetime import date

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


def fetch_product_order_count(
        start_date,
        end_date,
        count=10,
        sort_by_orders=False
        ) -> list | None:
    """
    Fetch the most ordered products within a date range.
    Parameters: start_date: str, end_date: str
    start_date -> Start date for the date range
    end_date -> End date for the date range
    """

    try:
        conn = get_database_connection()
        if not conn:
            return None
        cursor = conn.cursor()

        if not start_date:
            cursor.execute("SELECT MIN(order_date) FROM orders")
            start_date = cursor.fetchone()[0]
            if not start_date:
                logger.error("No orders found in the database.")
                return None

        if not end_date:
            end_date = date.today().strftime('%Y-%m-%d')

        query = """
            SELECT product_id, COUNT(product_id) AS total_orders
            FROM orders
            WHERE order_date BETWEEN ? AND ?
            GROUP BY product_id
            """

        if sort_by_orders:
            query += " ORDER BY total_orders DESC"

        query += " LIMIT ?"

        cursor.execute(query, (start_date, end_date, count))

        most_ordered = cursor.fetchall()

        close_database_connection(conn)

        return most_ordered

    except Exception as e:
        logger.error(f"Error fetching most ordered products: {e}")
        return None
