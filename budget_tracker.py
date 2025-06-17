try:
    #prompt the user to enter their monthly income
    monthly_income = int(input("Enter your monthly income: "))
except ValueError:
    print("Invalid input. Please enter a valid number for your monthly income.")
    exit()

#initialise a dictionary for expenses
expenses_dict = {}

try:
    #Ask the user to list their expenses
    expenses = input("Input your monthly expenses (name + amount), separating each expense with a comma, eg: 'Rent 10000, Transport 2000': ")
except ValueError:
    print("Invalid input. Please enter valid expenses in the correct format.")
    exit()

expenses_list = expenses.split(", ")

for expense in expenses_list:
    name, amount = expense.split(" ")
    expenses_dict[name] = int(amount)
    
money_spent = 0

money_spent = sum(expenses_dict.values())
balance = monthly_income - money_spent

# Output summary
print("\n--- Expense Summary ---")
for name, amount in expenses_dict.items():
    print(f"{name}: KES {amount}")

print(f"\nTotal spent: KES {money_spent}")
print(f"Remaining balance: KES {balance}")

# Budget advice
if money_spent > monthly_income:
    print(" Your expenses exceed your monthly income. Consider proper budgeting.")
elif money_spent == monthly_income:
    print(" You've spent your entire income. Try to save some next month.")
else:
    percent_spent = (money_spent / monthly_income) * 100
    print(f"You spent {percent_spent:.2f}% of your income.")
    print(" Good job keeping your expenses below your income!")