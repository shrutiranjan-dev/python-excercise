"""
Inventory Manager - Complete Solution
Manage product inventory using Python dictionaries.
"""

import itertools
from collections import defaultdict


class InventoryManager:
    """Manages product inventory using dictionaries."""

    def __init__(self):
        self._id_counter = itertools.count(1000)
        self.inventory = {}

    def _generate_id(self):
        return f"P{next(self._id_counter)}"

    def add_product(self, name, price, quantity, category):
        """Add a new product. Returns the product ID."""
        product_id = self._generate_id()
        self.inventory[product_id] = {
            "name": name,
            "price": price,
            "quantity": quantity,
            "category": category,
        }
        return product_id

    def add_product_with_id(self, product_id, name, price, quantity, category):
        """Add a product with a specific ID."""
        self.inventory[product_id] = {
            "name": name,
            "price": price,
            "quantity": quantity,
            "category": category,
        }
        return product_id

    def get_product(self, product_id):
        """Get product details by ID."""
        return self.inventory.get(product_id)

    def update_product(self, product_id, **kwargs):
        """Update product fields. Returns True if successful."""
        if product_id not in self.inventory:
            return False
        valid_keys = {"name", "price", "quantity", "category"}
        for key, value in kwargs.items():
            if key in valid_keys:
                self.inventory[product_id][key] = value
        return True

    def delete_product(self, product_id):
        """Delete a product by ID. Returns True if deleted."""
        if product_id in self.inventory:
            del self.inventory[product_id]
            return True
        return False

    def search_by_name(self, query):
        """Search products by name (partial match, case-insensitive)."""
        query = query.lower().strip()
        results = {}
        for pid, product in self.inventory.items():
            if query in product["name"].lower():
                results[pid] = product
        return results

    def search_by_category(self, category):
        """Search products by exact category (case-insensitive)."""
        category = category.lower().strip()
        results = {}
        for pid, product in self.inventory.items():
            if product["category"].lower() == category:
                results[pid] = product
        return results

    def get_low_stock_items(self, threshold=10):
        """Return products with quantity below threshold."""
        return {
            pid: product
            for pid, product in self.inventory.items()
            if product["quantity"] < threshold
        }

    def get_total_value(self):
        """Calculate total inventory value (price * quantity)."""
        return sum(
            product["price"] * product["quantity"]
            for product in self.inventory.values()
        )

    def get_products_by_category(self):
        """Group products by category using defaultdict."""
        grouped = defaultdict(dict)
        for pid, product in self.inventory.items():
            grouped[product["category"]][pid] = product
        return dict(grouped)

    def get_product_count(self):
        """Return total number of products."""
        return len(self.inventory)

    def get_total_quantity(self):
        """Return total quantity of all products."""
        return sum(p["quantity"] for p in self.inventory.values())

    def export_as_table(self):
        """Export inventory as a formatted table string."""
        lines = []
        lines.append(f"{'ID':<6} {'Name':<20} {'Price':<10} {'Qty':<6} Category")
        lines.append("-" * 60)
        for pid in sorted(self.inventory.keys()):
            p = self.inventory[pid]
            lines.append(
                f"{pid:<6} {p['name']:<20} ${p['price']:<7.2f} {p['quantity']:<6} {p['category']}"
            )
        return "\n".join(lines)

    def export_as_csv(self):
        """Export inventory as CSV string."""
        lines = ["id,name,price,quantity,category"]
        for pid, product in self.inventory.items():
            lines.append(
                f"{pid},{product['name']},{product['price']},"
                f"{product['quantity']},{product['category']}"
            )
        return "\n".join(lines)

    def get_report(self):
        """Generate a full inventory report."""
        lines = []
        lines.append("=== INVENTORY MANAGER ===")
        lines.append("")
        lines.append("--- Current Inventory ---")
        lines.append(self.export_as_table())

        lines.append("")
        lines.append(f"--- Search Results for \"lap\" ---")
        results = self.search_by_name("lap")
        if results:
            for pid, p in results.items():
                lines.append(
                    f"{pid} | {p['name']} | ${p['price']:.2f} | "
                    f"Qty: {p['quantity']} | {p['category']}"
                )
        else:
            lines.append("  (No results)")

        lines.append("")
        lines.append("--- Low Stock Alert (threshold < 10) ---")
        low = self.get_low_stock_items(10)
        if low:
            for pid, p in low.items():
                lines.append(f"  {pid} | {p['name']:20} | Qty: {p['quantity']}")
        else:
            lines.append("  (No low stock items)")

        lines.append("")
        total_value = self.get_total_value()
        lines.append(f"--- Total Inventory Value ---")
        lines.append(f"  ${total_value:,.2f}")

        lines.append("")
        lines.append("--- Inventory by Category ---")
        for category, products in self.get_products_by_category().items():
            lines.append(f"  {category}:")
            for pid, p in products.items():
                lines.append(f"    {pid}: {p['name']} - ${p['price']:.2f} x {p['quantity']}")

        return "\n".join(lines)


def main():
    manager = InventoryManager()

    # Add initial products
    manager.add_product("Laptop", 999.99, 5, "Electronics")
    manager.add_product("Mouse", 24.99, 50, "Accessories")
    manager.add_product("Keyboard", 79.99, 30, "Accessories")
    manager.add_product("Monitor", 299.99, 10, "Electronics")
    manager.add_product("USB Cable", 9.99, 100, "Accessories")

    print(manager.get_report())

    # Demonstrate update
    print("\n--- Updating Laptop quantity to 8 ---")
    manager.update_product("P1000", quantity=8)

    # Demonstrate delete
    print("\n--- Deleting USB Cable ---")
    manager.delete_product("P1004")

    # Show updated state
    print("\n\n=== UPDATED INVENTORY ===")
    print(manager.get_report())

    # CSV export
    print("\n")
    print("--- CSV Export ---")
    print(manager.export_as_csv())


if __name__ == "__main__":
    main()
