# Surprise Project: Expense Tracker

Build a command-line expense tracker that persists data to a JSON file.

## Requirements

### Core Features
1. **Add Expense** — Record date, category, amount, and description
2. **View All** — Display all expenses in a formatted table
3. **Filter** — Filter expenses by category or date range
4. **Calculate Totals** — Show total and average spending
5. **Category Breakdown** — Show spending grouped by category
6. **Save/Load** — Persist data to a JSON file
7. **Monthly Report** — Generate a summary report for a given month
8. **Data Persistence** — Expenses survive between program runs

### Data Fields
- `date` (YYYY-MM-DD)
- `category` (Food, Transport, Housing, Entertainment, Utilities, Other)
- `amount` (float)
- `description` (string)

### Example Flow
```
Expense Tracker
1. Add expense
2. View all
3. Filter by category
4. Filter by date range
5. Category breakdown
6. Monthly report
7. Totals & averages
8. Exit

Choose: 1
Date (YYYY-MM-DD): 2024-03-15
Category: Food
Amount: 25.50
Description: Lunch at cafe
Expense added!
```

### File Format
All data stored in `expenses.json` as a list of expense dicts.

### Bonus Ideas
- Edit/delete expenses
- Set monthly budget and track against it
- Export to CSV
- Visualize with simple ASCII bar charts
- Recurring expenses
- Currency conversion
