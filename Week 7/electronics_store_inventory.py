import importlib.util
from pathlib import Path


FILE_PATH = Path(__file__).with_name("A2W7A1.py")
SPEC = importlib.util.spec_from_file_location("inventory_module", FILE_PATH)
MODULE = importlib.util.module_from_spec(SPEC)
assert SPEC.loader is not None
SPEC.loader.exec_module(MODULE)


def create_inventory():
    inventory = {}
    MODULE.add_product(
        inventory,
        "P001",
        "Laptop X200",
        "Laptop",
        1299.99,
        0,
        {"color=silver": 3, "color=black": 2},
    )
    return inventory


def test_add_product_rejects_duplicate_id():
    inventory = create_inventory()
    added = MODULE.add_product(
        inventory,
        "P001",
        "Other laptop",
        "Laptop",
        999.99,
        0,
        {},
    )
    assert added is False


def test_add_product_calculates_stock():
    inventory = create_inventory()
    assert inventory["P001"]["stock"] == 5


def test_update_product_updates_price_and_variant():
    inventory = create_inventory()
    updated = MODULE.update_product(
        inventory,
        "P001",
        1199.99,
        {"color=black": 4},
    )
    assert updated is True
    assert inventory["P001"]["price"] == 1199.99
    assert inventory["P001"]["stock"] == 7


def test_update_product_rejects_unknown_variant():
    inventory = create_inventory()
    updated = MODULE.update_product(
        inventory,
        "P001",
        variants={"storage=1TB": 1},
    )
    assert updated is False


def test_delete_product():
    inventory = create_inventory()
    assert MODULE.delete_product(inventory, "P001") is True
    assert MODULE.delete_product(inventory, "P001") is False
