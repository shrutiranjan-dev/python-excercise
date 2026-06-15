"""Banking Utility Functions - Solution"""

from datetime import datetime
from typing import Dict, Tuple, Optional

_account_counter: int = 0


def _generate_account_number() -> str:
    global _account_counter
    _account_counter += 1
    date_part = datetime.now().strftime("%Y%m%d")
    return f"ACC-{date_part}-{_account_counter:03d}"


def _validate_account(account: dict) -> None:
    required_keys = {"account_number", "holder", "balance", "transactions"}
    if not isinstance(account, dict):
        raise TypeError("Account must be a dictionary")
    if not required_keys.issubset(account.keys()):
        raise ValueError(f"Account missing required keys: {required_keys - account.keys()}")


def _record_transaction(account: dict, txn_type: str, amount: float) -> None:
    account["transactions"].append({
        "type": txn_type,
        "amount": amount,
        "balance_after": account["balance"],
        "timestamp": datetime.now().isoformat(),
    })


def create_account(holder: str, initial_deposit: float = 0.0) -> dict:
    """Create a new bank account.

    Args:
        holder: Account holder's name
        initial_deposit: Starting balance (must be >= 0)

    Returns:
        Account dictionary with account_number, holder, balance, transactions
    """
    if initial_deposit < 0:
        raise ValueError("Initial deposit cannot be negative")

    account = {
        "account_number": _generate_account_number(),
        "holder": holder,
        "balance": initial_deposit,
        "transactions": [],
    }

    if initial_deposit > 0:
        _record_transaction(account, "deposit", initial_deposit)

    return account


def deposit(account: dict, amount: float) -> dict:
    """Deposit money into an account.

    Args:
        account: Account dictionary
        amount: Amount to deposit (must be > 0)

    Returns:
        Updated account dictionary
    """
    _validate_account(account)
    if amount <= 0:
        raise ValueError("Deposit amount must be positive")

    account["balance"] += amount
    _record_transaction(account, "deposit", amount)
    return account


def withdraw(account: dict, amount: float) -> dict:
    """Withdraw money from an account with overdraft protection.

    Args:
        account: Account dictionary
        amount: Amount to withdraw (must be > 0)

    Returns:
        Updated account dictionary
    """
    _validate_account(account)
    if amount <= 0:
        raise ValueError("Withdrawal amount must be positive")
    if amount > account["balance"]:
        raise ValueError(f"Insufficient funds. Balance: {account['balance']:.2f}, Requested: {amount:.2f}")

    account["balance"] -= amount
    _record_transaction(account, "withdrawal", amount)
    return account


def transfer(from_acc: dict, to_acc: dict, amount: float) -> Tuple[dict, dict]:
    """Transfer money between two accounts.

    Args:
        from_acc: Source account
        to_acc: Destination account
        amount: Amount to transfer (must be > 0)

    Returns:
        Tuple of (from_acc, to_acc)
    """
    _validate_account(from_acc)
    _validate_account(to_acc)
    if amount <= 0:
        raise ValueError("Transfer amount must be positive")

    withdraw(from_acc, amount)
    deposit(to_acc, amount)
    return from_acc, to_acc


def calculate_interest(balance: float, rate: float, years: int) -> float:
    """Calculate compound interest.

    Args:
        balance: Starting balance
        rate: Annual interest rate in percent (e.g., 5 for 5%)
        years: Number of years

    Returns:
        Balance after compound interest
    """
    return balance * (1 + rate / 100) ** years


def generate_statement(account: dict) -> str:
    """Generate a formatted account statement.

    Args:
        account: Account dictionary

    Returns:
        Formatted statement string
    """
    _validate_account(account)
    lines = []
    lines.append("=== ACCOUNT STATEMENT ===")
    lines.append(f"Account: {account['account_number']}")
    lines.append(f"Holder: {account['holder']}")
    lines.append(f"Balance: ${account['balance']:,.2f}")
    lines.append("")

    total_deposits = 0.0
    total_withdrawals = 0.0

    if account["transactions"]:
        lines.append("Transactions:")
        for i, txn in enumerate(account["transactions"], 1):
            ts = txn["timestamp"][:19] if "T" in txn["timestamp"] else txn["timestamp"]
            txn_type = txn["type"].upper()
            amount = txn["amount"]
            bal = txn["balance_after"]
            lines.append(f"  {i}. {ts}: {txn_type:11} ${amount:>8,.2f}  Balance: ${bal:>8,.2f}")

            if txn["type"] == "deposit":
                total_deposits += amount
            else:
                total_withdrawals += amount
    else:
        lines.append("No transactions yet.")

    lines.append("")
    lines.append("Summary:")
    lines.append(f"  Total Deposits:     ${total_deposits:>8,.2f}")
    lines.append(f"  Total Withdrawals:  ${total_withdrawals:>8,.2f}")
    lines.append(f"  Net Change:         ${total_deposits - total_withdrawals:>8,.2f}")

    return "\n".join(lines)


def main():
    alice = create_account("Alice Johnson", 1000)
    bob = create_account("Bob Smith", 500)

    deposit(alice, 2000)
    withdraw(alice, 500)
    withdraw(bob, 100)
    transfer(alice, bob, 250)

    print(generate_statement(alice))
    print()
    print(generate_statement(bob))

    interest = calculate_interest(1000, 5, 2)
    print(f"\nInterest on $1,000 at 5% for 2 years: ${interest:.2f}")


if __name__ == "__main__":
    main()
