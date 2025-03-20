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

## Function Documentation

### Functions to Be Implemented

The implementation will be on the following functions:

1. **Add Income**
   - Function Name: `add_income(data)`
   - Description: Adds an income transaction to the `transactions` list and updates the `balance`.
   - Parameters:
     - `data`: The `budget_data` dictionary.
   - Returns: Updated `budget_data` dictionary.

2. **Add Expense**
   - Function Name: `add_expense(data)`
   - Description: Adds an expense transaction to the `transactions` list and updates the `balance`.
   - Parameters:
     - `data`: The `budget_data` dictionary.
   - Returns: Updated `budget_data` dictionary.

3. **Show Balance**
   - Function Name: `show_balance(data)`
   - Description: Displays the current balance from the `budget_data` dictionary.
   - Parameters:
     - `data`: The `budget_data` dictionary.
   - Returns: `None` (This function only prints the balance and does not modify or return any data.)

4. **Show Transaction History**
   - Function Name: `show_transaction_history(data)`
   - Description: Displays all transactions stored in the `transactions` list.
   - Parameters:
     - `data`: The `budget_data` dictionary.
   - Returns: `None` (This function only prints the transaction history and does not modify or return any data.)














