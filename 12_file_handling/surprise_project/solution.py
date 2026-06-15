"""
Expense Tracker - Complete Solution
Persistent command-line expense tracking system using JSON file storage.
"""

import json
import os
from datetime import datetime
from pathlib import Path


class ExpenseTracker:
    def __init__(self, data_file="expenses.json"):
        self.data_file = Path(data_file)
        self.expenses = []
        self.categories = [
            "Food", "Transport", "Housing", "Entertainment", "Utilities", "Other"
        ]
        self._load()

    def _load(self):
        if self.data_file.exists():
            with open(self.data_file, "r", encoding="utf-8") as f:
                self.expenses = json.load(f)
        else:
            self.expenses = []

    def _save(self):
        with open(self.data_file, "w", encoding="utf-8") as f:
            json.dump(self.expenses, f, indent=2)

    def _validate_date(self, date_str):
        try:
            datetime.strptime(date_str, "%Y-%m-%d")
            return True
        except ValueError:
            return False

    def add_expense(self, date, category, amount, description):
        if not self._validate_date(date):
            return "Invalid date format. Use YYYY-MM-DD."
        if category not in self.categories:
            return f"Invalid category. Choose from: {', '.join(self.categories)}"
        try:
            amount = float(amount)
            if amount <= 0:
                return "Amount must be positive."
        except ValueError:
            return "Invalid amount. Must be a number."

        expense = {
            "id": len(self.expenses) + 1,
            "date": date,
            "category": category,
            "amount": round(amount, 2),
            "description": description
        }
        self.expenses.append(expense)
        self._save()
        return f"Expense added: ${amount:.2f} for {category}"

    def view_all(self):
        if not self.expenses:
            return "No expenses recorded."
        lines = [f"{'ID':<4} {'Date':<12} {'Category':<16} {'Amount':<10} Description"]
        lines.append("-" * 70)
        for e in self.expenses:
            lines.append(
                f"{e['id']:<4} {e['date']:<12} {e['category']:<16} "
                f"${e['amount']:<8.2f} {e['description']}"
            )
        return "\n".join(lines)

    def filter_by_category(self, category):
        filtered = [e for e in self.expenses if e["category"].lower() == category.lower()]
        if not filtered:
            return f"No expenses in category '{category}'."
        lines = [f"{'ID':<4} {'Date':<12} {'Amount':<10} Description"]
        lines.append("-" * 50)
        for e in filtered:
            lines.append(f"{e['id']:<4} {e['date']:<12} ${e['amount']:<8.2f} {e['description']}")
        total = sum(e["amount"] for e in filtered)
        lines.append(f"\nTotal for {category}: ${total:.2f}")
        return "\n".join(lines)

    def filter_by_date_range(self, start_date, end_date):
        if not self._validate_date(start_date) or not self._validate_date(end_date):
            return "Invalid date format. Use YYYY-MM-DD."
        filtered = [
            e for e in self.expenses
            if start_date <= e["date"] <= end_date
        ]
        if not filtered:
            return f"No expenses between {start_date} and {end_date}."
        lines = [f"{'ID':<4} {'Date':<12} {'Category':<16} {'Amount':<10} Description"]
        lines.append("-" * 70)
        for e in filtered:
            lines.append(
                f"{e['id']:<4} {e['date']:<12} {e['category']:<16} "
                f"${e['amount']:<8.2f} {e['description']}"
            )
        total = sum(e["amount"] for e in filtered)
        lines.append(f"\nTotal: ${total:.2f}")
        return "\n".join(lines)

    def category_breakdown(self):
        if not self.expenses:
            return "No expenses recorded."
        breakdown = {}
        for e in self.expenses:
            cat = e["category"]
            breakdown[cat] = breakdown.get(cat, 0) + e["amount"]

        lines = ["Category Breakdown"]
        lines.append("-" * 40)
        grand_total = 0
        for cat in sorted(breakdown.keys()):
            amt = breakdown[cat]
            grand_total += amt
            bar = "#" * int(amt / 10)
            lines.append(f"  {cat:<16} ${amt:<8.2f} {bar}")
        lines.append("-" * 40)
        lines.append(f"  {'TOTAL':<16} ${grand_total:.2f}")
        return "\n".join(lines)

    def monthly_report(self, year, month):
        prefix = f"{year}-{month:02d}"
        filtered = [e for e in self.expenses if e["date"].startswith(prefix)]

        if not filtered:
            return f"No expenses for {year}-{month:02d}."

        lines = [f"Monthly Report: {year}-{month:02d}"]
        lines.append("=" * 50)

        by_category = {}
        for e in filtered:
            by_category.setdefault(e["category"], []).append(e)

        grand_total = 0
        for cat in sorted(by_category.keys()):
            items = by_category[cat]
            cat_total = sum(e["amount"] for e in items)
            grand_total += cat_total
            lines.append(f"\n{cat}: ${cat_total:.2f} ({len(items)} transactions)")
            for e in items:
                lines.append(f"  {e['date']} ${e['amount']:<8.2f} {e['description']}")

        lines.append("\n" + "=" * 50)
        lines.append(f"GRAND TOTAL: ${grand_total:.2f}")
        lines.append(f"AVERAGE PER TRANSACTION: ${grand_total / len(filtered):.2f}")
        lines.append(f"TOTAL TRANSACTIONS: {len(filtered)}")

        return "\n".join(lines)

    def totals_and_averages(self):
        if not self.expenses:
            return "No expenses recorded."
        total = sum(e["amount"] for e in self.expenses)
        avg = total / len(self.expenses)
        dates = [e["date"] for e in self.expenses]
        return (
            f"Total Expenses: ${total:.2f}\n"
            f"Average per transaction: ${avg:.2f}\n"
            f"Transaction count: {len(self.expenses)}\n"
            f"Date range: {min(dates)} to {max(dates)}"
        )


def main():
    tracker = ExpenseTracker()

    while True:
        print("\n" + "=" * 40)
        print("  EXPENSE TRACKER")
        print("=" * 40)
        print("1. Add expense")
        print("2. View all")
        print("3. Filter by category")
        print("4. Filter by date range")
        print("5. Category breakdown")
        print("6. Monthly report")
        print("7. Totals & averages")
        print("8. Exit")
        print("-" * 40)

        choice = input("Choose (1-8): ").strip()

        if choice == "1":
            date = input("Date (YYYY-MM-DD): ").strip()
            print(f"Categories: {', '.join(tracker.categories)}")
            category = input("Category: ").strip()
            amount = input("Amount: ").strip()
            description = input("Description: ").strip()
            print(tracker.add_expense(date, category, amount, description))

        elif choice == "2":
            print(tracker.view_all())

        elif choice == "3":
            category = input("Category to filter: ").strip()
            print(tracker.filter_by_category(category))

        elif choice == "4":
            start = input("Start date (YYYY-MM-DD): ").strip()
            end = input("End date (YYYY-MM-DD): ").strip()
            print(tracker.filter_by_date_range(start, end))

        elif choice == "5":
            print(tracker.category_breakdown())

        elif choice == "6":
            year = input("Year (YYYY): ").strip()
            month = input("Month (MM): ").strip()
            try:
                print(tracker.monthly_report(int(year), int(month)))
            except ValueError:
                print("Invalid year or month.")

        elif choice == "7":
            print(tracker.totals_and_averages())

        elif choice == "8":
            print("Goodbye!")
            break

        else:
            print("Invalid choice. Please enter 1-8.")


if __name__ == "__main__":
    main()
