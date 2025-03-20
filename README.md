# Budget Manager

## Data Structure:
The budget manager stores financial transactions in a dictionary:

### Metadata  
- `balance`: The current balance of the budget (e.g., `500`).  
- `payment_method`: The default payment method used for transactions (e.g., `"Credit Card"`).  

### Transactions  
Each transaction in the `transactions` list contains:  
- `type`: The type of transaction (`"income"` or `"expense"`).  
- `cashflow`: The amount of money involved in the transaction (e.g., `1000`).  
- `label`: A short description or category for the transaction (e.g., `"Salary"`).  

## Example:  
```python
budget_data = {
   "metadata": {
        "balance": 500,
        "payment_method": "Credit Card"
   },
   "transactions": [
        {
         "type": "income",
         "cashflow": 1000,
         "label": "Salary"
       },
        {
           "type": "expense",
           "cashflow": 500,
           "label": "Groceries"
        }
    ]
}
