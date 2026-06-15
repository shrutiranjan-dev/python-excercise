# Surprise Project: Inventory Manager

## Overview
Build an inventory management system using Python dictionaries. This project demonstrates CRUD operations, nested dicts, searching/filtering, and report generation — skills essential for working with JSON-like data in AI/ML applications.

## Requirements

1. **Product inventory** stored as a dict where:
   - Key = Product ID (auto-generated or user-provided)
   - Value = Dict with name, price, quantity, category
2. **CRUD operations**:
   - **Create**: Add a new product
   - **Read**: View product details
   - **Update**: Modify product fields (price, quantity, etc.)
   - **Delete**: Remove a product
3. **Track**: Product name, price, quantity, category
4. **Search**:
   - By name (partial match, case-insensitive)
   - By category (exact match)
5. **Low stock alerts**: Show products with quantity below a threshold
6. **Total inventory value**: Sum of (price × quantity) for all products
7. **Data export**: Export inventory to a formatted string (CSV-like or table)

## Expected Output

```
=== INVENTORY MANAGER ===

--- Current Inventory ---
ID: P001 | Laptop      | $999.99 | Qty: 5  | Category: Electronics
ID: P002 | Mouse       | $24.99  | Qty: 50 | Category: Accessories
ID: P003 | Keyboard    | $79.99  | Qty: 30 | Category: Accessories
ID: P004 | Monitor     | $299.99 | Qty: 10 | Category: Electronics
ID: P005 | USB Cable   | $9.99   | Qty: 100| Category: Accessories

--- Search Results for "lap" ---
ID: P001 | Laptop | $999.99 | Qty: 5 | Electronics

--- Low Stock Alert (threshold < 10) ---
ID: P001 | Laptop      | Qty: 5
ID: P004 | Monitor     | Qty: 10

--- Total Inventory Value ---
$10,374.20

--- Inventory by Category ---
Electronics:
  P001: Laptop - $999.99 x 5
  P004: Monitor - $299.99 x 10
Accessories:
  P002: Mouse - $24.99 x 50
  P003: Keyboard - $79.99 x 30
  P005: USB Cable - $9.99 x 100
```

## Hints
- Use `itertools.count()` or a simple counter for auto-generating IDs
- String methods like `.lower()` and `.strip()` help with case-insensitive search
- `sum()` with a generator expression calculates total value
- Use f-strings with format specifiers like `:.2f` for currency
- `defaultdict(list)` helps group products by category
- The `tabulate` library (if allowed) makes pretty tables

## Extensions
- Save/load inventory from **JSON file**
- Implement **undo/redo** for operations (use a stack of dict snapshots)
- Add **sales tracking** (record sales and update quantities)
- Generate **restock report** (items with low stock + suggested order qty)
- Implement **price history tracking** using nested dicts
- Add **barcode scanning** simulation
- Create a **simple CLI menu** for interactive use
