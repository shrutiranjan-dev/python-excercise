# Surprise Project: Mini E-Commerce System

Build an object-oriented e-commerce system with file persistence.

## Requirements

### Classes

1. **Product**
   - Attributes: name, price, category, stock
   - Methods: update_stock, is_available, __str__, __repr__

2. **Customer**
   - Attributes: name, email, loyalty_points
   - Methods: add_points, redeem_points, __str__

3. **Cart**
   - Attributes: items (list of Product with quantities)
   - Methods: add_item, remove_item, update_quantity, clear, total, item_count

4. **Order**
   - Attributes: customer, items, total, status, date
   - Methods: process_order, generate_receipt, update_status

5. **Discount System**
   - Base Discount class (abstract)
   - PercentageDiscount (% off)
   - BOGODiscount (buy one get one)
   - LoyaltyDiscount (points-based)

6. **Inventory**
   - Track stock levels
   - Add/remove stock
   - Low-stock alerts (threshold)

7. **File Persistence**
   - Save/load all data to/from JSON
   - Products, customers, orders all persist

8. **Report Generation**
   - Sales report (total revenue, orders count)
   - Popular items (most ordered)
   - Customer summary (top spenders)

### Example Flow
```
=== Mini E-Commerce System ===
1. Add product
2. List products
3. Register customer
4. Create order
5. View orders
6. Generate reports
7. Add stock
8. Exit

Choose: 1
Product name: Laptop
Price: 999.99
Category: Electronics
Stock: 10
Product added!
```

### Bonus Ideas
- Search products by name/category
- Sort products by price
- Order history per customer
- Shopping cart per customer
- Return/refund system
- Tax calculation
- Rating/review system
