"""Loan Eligibility Checker - Solution"""


def get_user_input():
    income = float(input("Enter annual income: "))
    credit_score = int(input("Enter credit score (300-850): "))
    employment = input("Employment status (employed/self-employed/unemployed): ").strip().lower()
    existing_loans = int(input("Number of existing loans: "))
    return income, credit_score, employment, existing_loans


def determine_eligibility(income, credit_score, employment, existing_loans):
    if credit_score < 580:
        return "rejected", "Credit score too low"
    if employment == "unemployed" and income <= 0:
        return "rejected", "Unemployed with no income"
    if existing_loans >= 5:
        return "rejected", "Too many existing loans"
    if income < 15000 and credit_score < 650:
        return "rejected", "Income too low for credit score"
    if income < 15000 and credit_score >= 650:
        return "partial", "Partially eligible"
    if income < 50000:
        return "standard", "Standard eligibility"
    return "premium", "Premium eligibility"


def determine_risk_category(income, credit_score, existing_loans, eligibility):
    if eligibility == "rejected":
        return None
    if eligibility == "partial":
        return "High Risk"
    if credit_score >= 750 and income >= 50000 and existing_loans <= 2:
        return "Low Risk"
    return "Medium Risk"


def calculate_loan_amount(income, eligibility):
    match eligibility:
        case "premium":
            return income * 0.5
        case "standard":
            return income * 0.3
        case "partial":
            return income * 0.15
        case _:
            return 0.0


def get_interest_rate(risk_category):
    match risk_category:
        case "Low Risk":
            return 5
        case "Medium Risk":
            return 8
        case "High Risk":
            return 12
        case _:
            return 0


def generate_letter(status, risk, max_loan, interest):
    lines = [
        "=== LOAN DECISION LETTER ===",
        f"Status: {status}",
    ]
    if status == "APPROVED":
        lines.append(f"Risk Category: {risk}")
        lines.append(f"Max Loan Amount: ${max_loan:.2f}")
        lines.append(f"Interest Rate: {interest}%")
        lines.append("Terms: Standard repayment over 36 months")
    else:
        lines.append("We regret to inform you that your loan application has been denied.")
    return "\n".join(lines)


def main():
    income, credit_score, employment, existing_loans = get_user_input()

    eligibility, reason = determine_eligibility(income, credit_score, employment, existing_loans)

    risk = determine_risk_category(income, credit_score, existing_loans, eligibility)

    if eligibility == "rejected":
        status = "REJECTED"
        max_loan = 0
        interest = 0
    else:
        status = "APPROVED"
        max_loan = calculate_loan_amount(income, eligibility)
        interest = get_interest_rate(risk)

    letter = generate_letter(status, risk, max_loan, interest)
    print()
    print(letter)


if __name__ == "__main__":
    main()
