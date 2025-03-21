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

# def addIncome(totalIncome,discription):
#     totalIncome,discription=input("pls insert your income then split by , then insert description you want ..\n").split(",")
#     transactions.append(("income",int(totalIncome)),discription)



def showInstruction():
    print("1. Add Income\n"
          "2. Add Expense \n"
          "3. Show Balance \n"
          "4. Show Transaction History \n"
          "5. Exit"
)
    

    
def main():
    while True:
        showInstruction()
        inputUser=int(input("Pls select option: \n"))
        if(inputUser==1):
            AddIncome(budget_data)
        elif(input==2):
            totalExpense,discription=input("pls insert your expense then split by , then insert description you want ..\n").split(",")
            addExpense(totalExpense,discription)
        elif(input==3):
            print("show_balance funtion")
        elif(input==4):
            print("show_transations()")
        elif(input==5):
            break
        else:
            print("Invalid choice.Pls select a valid option.")