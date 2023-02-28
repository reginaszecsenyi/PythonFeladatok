"""
This module simulates the database of the CommandLine Shop
"""

# Termékek - azonosító: int, név: str, ár: float
DATA = [
    [1, 'Alma', 100.0],
    [2, 'Körte', 150.5],
    [3, 'Répa', 50.0],
    [4, 'Saláta', 185.0],
    [5, 'Kolbász', 250.5],
    [6, 'Zsemle', 15.0]
]


def get_all_item() -> list:
    pass


def get_item_by_(item_id: int) -> list:
    pass


def add_new(item: list) -> bool:
    pass


def remove_item_by_(item_id: int) -> bool:
    pass


def update_item(item: list) -> bool:
    pass