"""
sql_sim: A simulation tool for generating sales data and\
analyzing it through a dashboard.
"""

# Package metadata
__version__ = "0.1.0"
__author__ = "Pranshu Jha"
__email__ = "hello@pranshujha.com"

# Import key components for easier access
from .database import (
    initialise_database,
    get_database_connection,
    close_database_connection,
    populate_customers_table,
    populate_products_table,
)

# Optional: Define what gets imported when `from sql_sim import *` is used
__all__ = [
    "initialise_database",
    "get_database_connection",
    "close_database_connection",
    "populate_customers_table",
    "populate_products_table"
]
