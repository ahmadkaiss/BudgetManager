# BudgetManager

transactions = [
 ("income", 1000, "Salary"),
 ("expense", 500, "Rent"),
 ("expense", 200, "Groceries")
]

def addIncome(totalIncome,discription):
    totalIncome,discription=input("pls insert your income then split by , then insert description you want ..\n").split(",")
    transactions.append(("income",int(totalIncome)),discription)


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
        inputUser=int(input("Pls select number"))
        if(inputUser==1):
            AddIncome(totalIncome,discription)
        elif(input==2):
            totalExpense,discription=input("pls insert your expense then split by , then insert description you want ..\n").split(",")
            addExpense(totalExpense,discription)
        




  



