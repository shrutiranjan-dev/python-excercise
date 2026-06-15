# Surprise Project: Loan Eligibility Checker

## Objective
Build a system that determines loan eligibility based on multiple financial and personal factors using conditionals.

## Requirements

### 1. Input
Take the following inputs from the user:
- **Income**: Annual income in dollars (float)
- **Credit Score**: FICO score 300-850 (int)
- **Employment Status**: "employed", "self-employed", "unemployed" (string)
- **Existing Loans**: Number of existing loans (int)

### 2. Eligibility Rules

| Condition | Result |
|---|---|
| Credit score < 580 | Automatically rejected |
| Unemployed with no income | Automatically rejected |
| Existing loans >= 5 | Automatically rejected |
| Income < 15000 and credit score < 650 | Rejected |
| Income < 15000 and credit score >= 650 | Partial eligibility |
| Income >= 15000 and < 50000 | Standard eligibility |
| Income >= 50000 | Premium eligibility |

### 3. Risk Category
- **Low Risk**: Credit score >= 750 AND income >= 50000 AND existing loans <= 2
- **Medium Risk**: All other eligible applicants
- **High Risk**: Partially eligible applicants

### 4. Max Loan Amount
- Premium: `income * 0.5`
- Standard: `income * 0.3`
- Partial: `income * 0.15`
- Rejected: 0

### 5. Output
Generate an approval/rejection letter with:
- Applicant status
- Risk category (if eligible)
- Max loan amount
- Interest rate suggestion (Low risk: 5%, Medium risk: 8%, High risk: 12%)

## Example Run
```
Enter annual income: 60000
Enter credit score (300-850): 720
Employment status (employed/self-employed/unemployed): employed
Number of existing loans: 1

=== LOAN DECISION LETTER ===
Status: APPROVED
Risk Category: Medium Risk
Max Loan Amount: $18000.00
Interest Rate: 8%
Terms: Standard repayment over 36 months
```

## Challenge Extensions
1. Add a co-signer option that improves eligibility
2. Implement debt-to-income ratio check (monthly debt payments / monthly income)
3. Add loan purpose (home, car, personal) with different rates
4. Support multiple currencies with exchange rate conversion
