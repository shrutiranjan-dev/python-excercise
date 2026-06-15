# Surprise Project: Banking Utility Functions

## Objective
Build a reusable banking utility module with functions for account management, transactions, interest calculation, and statement generation.

## Requirements

### Implement These Functions:

#### 1. `create_account(holder: str, initial_deposit: float) -> dict`
- Create an account dict with: `account_number`, `holder`, `balance`, `transactions`
- Account number should be auto-generated (use a global counter or timestamp)
- Initial deposit must be >= 0
- Record the initial deposit as the first transaction

#### 2. `deposit(account: dict, amount: float) -> dict`
- Add amount to account balance
- Amount must be > 0
- Record transaction: `{"type": "deposit", "amount": amount, "balance_after": new_balance}`
- Return the updated account

#### 3. `withdraw(account: dict, amount: float) -> dict`
- Subtract amount from account balance
- **Overdraft protection**: Cannot withdraw more than the current balance
- Amount must be > 0
- Record transaction
- Return the updated account

#### 4. `transfer(from_acc: dict, to_acc: dict, amount: float) -> tuple`
- Withdraw from source, deposit to destination
- Return `(from_acc, to_acc)` tuple
- Must handle insufficient funds
- Record transactions on both accounts

#### 5. `calculate_interest(balance: float, rate: float, years: int) -> float`
- Return the balance after `years` of compound interest at `rate`%
- Formula: `balance * (1 + rate/100) ** years`

#### 6. `generate_statement(account: dict) -> str`
- Return a formatted string statement with:
  - Account header (number, holder)
  - Current balance
  - Transaction history (numbered, with dates)
  - Summary (total deposits, total withdrawals)

### Validation Requirements
- All monetary amounts must be positive for deposits/withdrawals/transfers
- Cannot overdraw (withdraw more than balance)
- Account must be a valid dict with required keys
- Type hints and docstrings on every function

## Example Output

```
=== ACCOUNT STATEMENT ===
Account: ACC-20240315-001
Holder: Alice Johnson
Balance: $2,450.00

Transactions:
  1. 2024-03-15 10:30: DEPOSIT    $1,000.00  Balance: $1,000.00
  2. 2024-03-15 10:31: WITHDRAWAL $500.00    Balance: $500.00
  3. 2024-03-15 10:32: DEPOSIT    $2,000.00  Balance: $2,500.00
  4. 2024-03-15 10:33: WITHDRAWAL $50.00     Balance: $2,450.00

Summary:
  Total Deposits:     $3,000.00
  Total Withdrawals:  $550.00
  Net Change:         $2,450.00
```

## Challenge Extensions
1. Add `apply_monthly_interest(account, annual_rate)` that applies 1/12 of annual rate
2. Add `close_account(account)` that prevents further transactions
3. Add `search_transactions(account, min_amount=None, max_amount=None, type=None)`
4. Implement `schedule_transfer(from_acc, to_acc, amount, interval_days)` for recurring transfers
