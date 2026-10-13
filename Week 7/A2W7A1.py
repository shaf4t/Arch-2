import json
import os
import sys
import unittest


def get_inventory() -> dict:
    with open(os.path.join(sys.path[0], "inventory.json")) as json_file:
        return json.load(json_file)


def add_product(
    inventory: dict,
    product_id: str,
    name: str,
    category: str,
    price: float,
    stock: int,
    variants: dict,
) -> bool:
    if product_id in inventory:
        return False

    inventory[product_id] = {
        "name": name,
        "category": category,
        "price": price,
        "stock": sum(variants.values()),
        "variants": variants.copy(),
    }
    return True


def update_product(
    inventory: dict,
    product_id: str,
    price: float = None,
    variants: dict = None,
) -> bool:
    if product_id not in inventory:
        return False

    product = inventory[product_id]
    if variants is not None:
        if any(variant not in product["variants"] for variant in variants):
            return False
        product["variants"].update(variants)
        product["stock"] = sum(product["variants"].values())

    if price is not None:
        product["price"] = price
    return True


def delete_product(inventory: dict, product_id: str) -> bool:
    if product_id not in inventory:
        return False
    del inventory[product_id]
    return True


def read_variants() -> dict:
    variants = {}
    while input("Do you want to enter a variant (yes/no)?").lower() == "yes":
        variant_name = input("Enter variant name:")
        variant_stock = int(input("Enter variant stock level:"))
        variants[variant_name] = variant_stock
    return variants


def main() -> None:
    inventory = get_inventory()

    while True:
        print("[A] Add a new product")
        print("[U] Update an existing product")
        print("[D] Delete an existing product")
        print("[Q] Quit the program")
        choice = input("").upper()

        if choice == "A":
            product_id = input("Input product ID:")
            name = input("Input product name:")
            category = input("Input product category:")
            price = float(input("Input product price:"))
            variants = read_variants()
            stock = sum(variants.values())
            if add_product(
                inventory,
                product_id,
                name,
                category,
                price,
                stock,
                variants,
            ):
                print("Product added!")
            else:
                print("Product ID already exists")
        elif choice == "U":
            product_id = input("Input product ID:")
            if product_id not in inventory:
                print("ID doesn't exist")
                continue
            price = float(input("Input product price:"))
            variants = read_variants()
            if update_product(inventory, product_id, price, variants):
                print("Product updated!")
            else:
                print("ID doesn't exist")
        elif choice == "D":
            product_id = input("Input product ID:")
            if delete_product(inventory, product_id):
                print("Product deleted!")
            else:
                print("ID doesn't exist")
        elif choice == "Q":
            break


if __name__ == "__main__":
    main()


class TestInventoryFunctions(unittest.TestCase):
    def setUp(self):
        self.inventory = {}
        add_product(
            self.inventory,
            "P001",
            "Laptop X200",
            "Laptop",
            1299.99,
            0,
            {"color=silver": 3, "color=black": 2},
        )

    def test_add_product_rejects_duplicate_id(self):
        added = add_product(
            self.inventory,
            "P001",
            "Other laptop",
            "Laptop",
            999.99,
            0,
            {},
        )
        self.assertFalse(added)

    def test_add_product_calculates_stock(self):
        self.assertEqual(self.inventory["P001"]["stock"], 5)

    def test_update_product_updates_price_and_variant(self):
        updated = update_product(
            self.inventory,
            "P001",
            1199.99,
            {"color=black": 4},
        )
        self.assertTrue(updated)
        self.assertEqual(self.inventory["P001"]["price"], 1199.99)
        self.assertEqual(self.inventory["P001"]["stock"], 7)

    def test_update_product_rejects_unknown_variant(self):
        updated = update_product(
            self.inventory,
            "P001",
            variants={"storage=1TB": 1},
        )
        self.assertFalse(updated)

    def test_delete_product(self):
        self.assertTrue(delete_product(self.inventory, "P001"))
        self.assertFalse(delete_product(self.inventory, "P001"))
