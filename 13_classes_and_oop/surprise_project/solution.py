"""
Mini E-Commerce System - Complete Solution
Object-Oriented design with file persistence and reports.
"""

import json
from abc import ABC, abstractmethod
from datetime import datetime
from pathlib import Path


# ============================================================
# Product Class
# ============================================================

class Product:
    def __init__(self, name, price, category, stock=0, product_id=None):
        self.product_id = product_id or id(self)
        self.name = name
        self.price = price
        self.category = category
        self.stock = stock

    def update_stock(self, quantity):
        self.stock += quantity
        if self.stock < 0:
            self.stock = 0
        return self.stock

    def is_available(self, quantity=1):
        return self.stock >= quantity

    def to_dict(self):
        return {
            "product_id": self.product_id,
            "name": self.name,
            "price": self.price,
            "category": self.category,
            "stock": self.stock,
        }

    @classmethod
    def from_dict(cls, data):
        return cls(
            name=data["name"],
            price=data["price"],
            category=data["category"],
            stock=data["stock"],
            product_id=data["product_id"],
        )

    def __str__(self):
        return f"{self.name} (${self.price:.2f}) - {self.stock} in stock"

    def __repr__(self):
        return f"Product('{self.name}', {self.price})"


# ============================================================
# Customer Class
# ============================================================

class Customer:
    def __init__(self, name, email, loyalty_points=0, customer_id=None):
        self.customer_id = customer_id or id(self)
        self.name = name
        self.email = email
        self.loyalty_points = loyalty_points

    def add_points(self, points):
        self.loyalty_points += points

    def redeem_points(self, points):
        if points > self.loyalty_points:
            raise ValueError("Not enough loyalty points")
        self.loyalty_points -= points
        return points * 0.01  # $0.01 per point

    def to_dict(self):
        return {
            "customer_id": self.customer_id,
            "name": self.name,
            "email": self.email,
            "loyalty_points": self.loyalty_points,
        }

    @classmethod
    def from_dict(cls, data):
        return cls(
            name=data["name"],
            email=data["email"],
            loyalty_points=data["loyalty_points"],
            customer_id=data["customer_id"],
        )

    def __str__(self):
        return f"{self.name} ({self.email}) - {self.loyalty_points} pts"


# ============================================================
# Cart Class
# ============================================================

class Cart:
    def __init__(self):
        self.items = []  # List of (Product, quantity) tuples

    def add_item(self, product, quantity=1):
        if not product.is_available(quantity):
            raise ValueError(f"Insufficient stock for {product.name}")
        for i, (p, q) in enumerate(self.items):
            if p.product_id == product.product_id:
                self.items[i] = (p, q + quantity)
                return
        self.items.append((product, quantity))

    def remove_item(self, product):
        self.items = [(p, q) for p, q in self.items if p.product_id != product.product_id]

    def update_quantity(self, product, quantity):
        for i, (p, q) in enumerate(self.items):
            if p.product_id == product.product_id:
                if quantity <= 0:
                    self.remove_item(product)
                else:
                    self.items[i] = (p, quantity)
                return
        raise ValueError(f"{product.name} not in cart")

    def clear(self):
        self.items.clear()

    @property
    def total(self):
        return sum(p.price * q for p, q in self.items)

    @property
    def item_count(self):
        return sum(q for _, q in self.items)

    def __str__(self):
        if not self.items:
            return "Cart is empty"
        lines = [f"{'Item':<20} {'Qty':<5} {'Price':<10} {'Total':<10}"]
        lines.append("-" * 45)
        for p, q in self.items:
            lines.append(f"{p.name:<20} {q:<5} ${p.price:<8.2f} ${p.price * q:<8.2f}")
        lines.append("-" * 45)
        lines.append(f"{'Total':<30} ${self.total:.2f}")
        return "\n".join(lines)


# ============================================================
# Discount System
# ============================================================

class Discount(ABC):
    @abstractmethod
    def apply(self, total):
        pass

    @abstractmethod
    def description(self):
        pass


class PercentageDiscount(Discount):
    def __init__(self, percent):
        self.percent = percent

    def apply(self, total):
        return total * (1 - self.percent / 100)

    def description(self):
        return f"{self.percent}% off"


class BOGODiscount(Discount):
    """Buy One Get One: every 2 items, one is free (cheapest item)."""

    def __init__(self, items):
        self.items = items

    def apply(self, total):
        prices = sorted([p.price for p, q in self.items for _ in range(q)], reverse=True)
        discount = sum(prices[1::2])
        return total - discount

    def description(self):
        return "Buy One Get One Free"


class LoyaltyDiscount(Discount):
    def __init__(self, customer, points_to_redeem=0):
        self.customer = customer
        self.points_to_redeem = points_to_redeem

    def apply(self, total):
        if self.points_to_redeem > 0:
            discount = self.customer.redeem_points(self.points_to_redeem)
            return max(0, total - discount)
        return total

    def description(self):
        return f"Loyalty discount ({self.points_to_redeem} pts)"


# ============================================================
# Order Class
# ============================================================

class Order:
    def __init__(self, order_id, customer, cart_items, discounts=None):
        self.order_id = order_id
        self.customer = customer
        self.items = cart_items  # List of (Product, quantity)
        self.discounts = discounts or []
        self._subtotal = sum(p.price * q for p, q in self.items)
        self._discount_total = self._calculate_discounts()
        self.total = self._subtotal - self._discount_total
        self.status = "pending"
        self.date = datetime.now().isoformat()

    def _calculate_discounts(self):
        total_discount = 0
        for d in self.discounts:
            discounted = d.apply(self._subtotal)
            total_discount += self._subtotal - discounted
        return total_discount

    def process_order(self):
        for product, quantity in self.items:
            product.update_stock(-quantity)
        points_earned = int(self.total)
        self.customer.add_points(points_earned)
        self.status = "completed"
        return points_earned

    def update_status(self, new_status):
        valid_statuses = ["pending", "completed", "shipped", "delivered", "cancelled"]
        if new_status not in valid_statuses:
            raise ValueError(f"Invalid status: {new_status}")
        self.status = new_status

    def generate_receipt(self):
        lines = []
        lines.append("=" * 50)
        lines.append(f"  ORDER RECEIPT #{self.order_id}")
        lines.append(f"  Date: {self.date[:19]}")
        lines.append(f"  Customer: {self.customer.name}")
        lines.append("=" * 50)
        lines.append(f"{'Item':<25} {'Qty':<5} {'Price':<10}")
        lines.append("-" * 50)
        for p, q in self.items:
            lines.append(f"{p.name:<25} {q:<5} ${p.price:<8.2f}")
        lines.append("-" * 50)
        lines.append(f"{'Subtotal':<35} ${self._subtotal:.2f}")
        if self._discount_total > 0:
            for d in self.discounts:
                lines.append(f"  Discount ({d.description()}): -${self._discount_total:.2f}")
        lines.append(f"{'TOTAL':<35} ${self.total:.2f}")
        lines.append(f"{'Points Earned':<35} {int(self.total)}")
        lines.append(f"{'Status':<35} {self.status}")
        lines.append("=" * 50)
        lines.append("  Thank you for your purchase!")
        return "\n".join(lines)

    def to_dict(self):
        return {
            "order_id": self.order_id,
            "customer_id": self.customer.customer_id,
            "items": [(p.product_id, q) for p, q in self.items],
            "subtotal": self._subtotal,
            "total": self.total,
            "status": self.status,
            "date": self.date,
        }

    def __str__(self):
        return f"Order #{self.order_id} - {self.customer.name} - ${self.total:.2f} ({self.status})"


# ============================================================
# Inventory Management
# ============================================================

class Inventory:
    def __init__(self, low_stock_threshold=5):
        self.products = {}
        self.threshold = low_stock_threshold

    def add_product(self, product):
        self.products[product.product_id] = product

    def remove_product(self, product_id):
        return self.products.pop(product_id, None)

    def get_product(self, product_id):
        return self.products.get(product_id)

    def find_by_name(self, name):
        return [p for p in self.products.values() if name.lower() in p.name.lower()]

    def find_by_category(self, category):
        return [p for p in self.products.values() if p.category.lower() == category.lower()]

    def low_stock_items(self):
        return [p for p in self.products.values() if p.stock <= self.threshold]

    def total_value(self):
        return sum(p.price * p.stock for p in self.products.values())


# ============================================================
# Report Generation
# ============================================================

class ReportGenerator:
    @staticmethod
    def sales_report(orders):
        if not orders:
            return "No orders to report."

        total_revenue = sum(o.total for o in orders)
        completed = [o for o in orders if o.status == "completed"]

        lines = ["SALES REPORT", "=" * 40]
        lines.append(f"Total orders: {len(orders)}")
        lines.append(f"Completed orders: {len(completed)}")
        lines.append(f"Total revenue: ${total_revenue:.2f}")
        lines.append(f"Average order value: ${total_revenue / len(orders):.2f}")

        if completed:
            dates = [o.date[:10] for o in completed]
            lines.append(f"Date range: {min(dates)} to {max(dates)}")

        return "\n".join(lines)

    @staticmethod
    def popular_items(orders, top_n=5):
        item_counts = {}
        for o in orders:
            for p, q in o.items:
                item_counts[p.name] = item_counts.get(p.name, 0) + q

        sorted_items = sorted(item_counts.items(), key=lambda x: x[1], reverse=True)

        lines = [f"TOP {top_n} MOST POPULAR ITEMS", "=" * 40]
        for i, (name, count) in enumerate(sorted_items[:top_n], 1):
            lines.append(f"{i}. {name} - ordered {count} times")

        return "\n".join(lines)

    @staticmethod
    def customer_summary(orders):
        customer_totals = {}
        customer_orders = {}

        for o in orders:
            cid = o.customer.customer_id
            customer_totals[cid] = customer_totals.get(cid, 0) + o.total
            if cid not in customer_orders:
                customer_orders[cid] = {"customer": o.customer, "orders": [], "count": 0}
            customer_orders[cid]["orders"].append(o)
            customer_orders[cid]["count"] += 1

        sorted_customers = sorted(
            customer_orders.values(),
            key=lambda x: customer_totals[x["customer"].customer_id],
            reverse=True,
        )

        lines = ["CUSTOMER SUMMARY", "=" * 50]
        for entry in sorted_customers:
            c = entry["customer"]
            total = customer_totals[c.customer_id]
            lines.append(f"{c.name:<20} Orders: {entry['count']:<3} Total: ${total:<8.2f} Points: {c.loyalty_points}")

        return "\n".join(lines)


# ============================================================
# Main Application
# ============================================================

class ECommerceSystem:
    def __init__(self, data_file="ecommerce_data.json"):
        self.data_file = Path(data_file)
        self.inventory = Inventory()
        self.customers = {}
        self.orders = []
        self.next_order_id = 1
        self._load()

    def _load(self):
        if self.data_file.exists():
            with open(self.data_file, "r", encoding="utf-8") as f:
                data = json.load(f)

            for p_data in data.get("products", []):
                product = Product.from_dict(p_data)
                self.inventory.add_product(product)

            for c_data in data.get("customers", []):
                customer = Customer.from_dict(c_data)
                self.customers[customer.customer_id] = customer

            self.next_order_id = data.get("next_order_id", 1)

            for o_data in data.get("orders", []):
                customer = self.customers.get(o_data["customer_id"])
                if customer:
                    items = []
                    for pid, qty in o_data["items"]:
                        product = self.inventory.get_product(pid)
                        if product:
                            items.append((product, qty))
                    order = Order(
                        order_id=o_data["order_id"],
                        customer=customer,
                        cart_items=items,
                    )
                    order.total = o_data["total"]
                    order.status = o_data["status"]
                    order.date = o_data["date"]
                    self.orders.append(order)

    def _save(self):
        data = {
            "products": [p.to_dict() for p in self.inventory.products.values()],
            "customers": [c.to_dict() for c in self.customers.values()],
            "orders": [o.to_dict() for o in self.orders],
            "next_order_id": self.next_order_id,
        }
        with open(self.data_file, "w", encoding="utf-8") as f:
            json.dump(data, f, indent=2)

    def add_product(self, name, price, category, stock):
        product = Product(name, float(price), category, int(stock))
        self.inventory.add_product(product)
        self._save()
        return f"Product '{name}' added!"

    def register_customer(self, name, email):
        customer = Customer(name, email)
        self.customers[customer.customer_id] = customer
        self._save()
        return f"Customer '{name}' registered!"

    def create_order(self, customer_id, product_ids_and_quantities, discount_type=None):
        customer = self.customers.get(customer_id)
        if not customer:
            return "Customer not found."

        cart = Cart()
        for pid, qty in product_ids_and_quantities:
            product = self.inventory.get_product(pid)
            if not product:
                return f"Product {pid} not found."
            try:
                cart.add_item(product, qty)
            except ValueError as e:
                return str(e)

        discounts = []
        if discount_type == "loyalty":
            points = min(customer.loyalty_points, int(cart.total * 100))
            discounts.append(LoyaltyDiscount(customer, points))

        order = Order(self.next_order_id, customer, cart.items, discounts)
        self.next_order_id += 1
        points = order.process_order()
        self.orders.append(order)
        self._save()

        return f"Order #{order.order_id} created! {points} points earned."

    def list_products(self):
        if not self.inventory.products:
            return "No products."
        lines = [f"{'ID':<12} {'Name':<25} {'Price':<10} {'Stock':<8} {'Category':<15}"]
        lines.append("-" * 70)
        for p in self.inventory.products.values():
            lines.append(f"{p.product_id:<12} {p.name:<25} ${p.price:<8.2f} {p.stock:<8} {p.category:<15}")
        return "\n".join(lines)

    def list_customers(self):
        if not self.customers:
            return "No customers."
        lines = [f"{'ID':<12} {'Name':<20} {'Email':<30} {'Points':<8}"]
        lines.append("-" * 70)
        for c in self.customers.values():
            lines.append(f"{c.customer_id:<12} {c.name:<20} {c.email:<30} {c.loyalty_points:<8}")
        return "\n".join(lines)

    def list_orders(self):
        if not self.orders:
            return "No orders."
        lines = [f"{'Order#':<8} {'Customer':<20} {'Total':<10} {'Status':<15} {'Date':<12}"]
        lines.append("-" * 65)
        for o in self.orders:
            lines.append(f"{o.order_id:<8} {o.customer.name:<20} ${o.total:<8.2f} {o.status:<15} {o.date[:10]:<12}")
        return "\n".join(lines)

    def generate_receipt(self, order_id):
        for o in self.orders:
            if o.order_id == order_id:
                return o.generate_receipt()
        return "Order not found."

    def generate_reports(self):
        parts = [
            ReportGenerator.sales_report(self.orders),
            "",
            ReportGenerator.popular_items(self.orders),
            "",
            ReportGenerator.customer_summary(self.orders),
        ]
        return "\n".join(parts)

    def add_stock(self, product_id, quantity):
        product = self.inventory.get_product(product_id)
        if not product:
            return "Product not found."
        product.update_stock(int(quantity))
        self._save()
        return f"{quantity} units added to '{product.name}'. New stock: {product.stock}"


def main():
    system = ECommerceSystem()

    while True:
        print("\n" + "=" * 40)
        print("  MINI E-COMMERCE SYSTEM")
        print("=" * 40)
        print("1.  Add product")
        print("2.  List products")
        print("3.  Register customer")
        print("4.  List customers")
        print("5.  Create order")
        print("6.  View orders")
        print("7.  Generate receipt")
        print("8.  Generate reports")
        print("9.  Add stock")
        print("10. Exit")
        print("-" * 40)

        choice = input("Choose (1-10): ").strip()

        if choice == "1":
            name = input("Product name: ").strip()
            price = input("Price: ").strip()
            category = input("Category: ").strip()
            stock = input("Stock: ").strip()
            print(system.add_product(name, price, category, stock))

        elif choice == "2":
            print("\n" + system.list_products())

        elif choice == "3":
            name = input("Customer name: ").strip()
            email = input("Email: ").strip()
            print(system.register_customer(name, email))

        elif choice == "4":
            print("\n" + system.list_customers())

        elif choice == "5":
            print(system.list_customers())
            cid = int(input("Customer ID: ").strip())
            print("\n" + system.list_products())
            items = []
            while True:
                pid = input("Product ID (or blank to finish): ").strip()
                if not pid:
                    break
                qty = int(input("Quantity: ").strip())
                items.append((int(pid), qty))
            discount = input("Discount type (none/loyalty): ").strip().lower()
            if discount not in ("loyalty",):
                discount = None
            print(system.create_order(cid, items, discount))

        elif choice == "6":
            print("\n" + system.list_orders())

        elif choice == "7":
            oid = int(input("Order ID: ").strip())
            print("\n" + system.generate_receipt(oid))

        elif choice == "8":
            print("\n" + system.generate_reports())

        elif choice == "9":
            print(system.list_products())
            pid = int(input("Product ID: ").strip())
            qty = int(input("Quantity to add: ").strip())
            print(system.add_stock(pid, qty))

        elif choice == "10":
            print("Goodbye!")
            break

        else:
            print("Invalid choice. Please enter 1-10.")


if __name__ == "__main__":
    main()
