
# Collections - C
financial_data = {
    "account_balance": 5000.0,
    "expenses": {
        "rent": 1000.0,
        "utilities": 300.0,
        "groceries": [100.0, 300.0, 100.0]
},
    "income": 3000.0
}

account_balace = financial_data["account_balance"]
income = financial_data["income"]
account_income = account_balace + income


rent = financial_data["expenses"]["rent"]
utilities = financial_data["expenses"]["utilities"]
groceries = sum(financial_data["expenses"]["groceries"])

expenses = rent + utilities + groceries

if account_balace > expenses:
    print("True")
else:
    print("False")



# Loops - 4
total = 0
while True:  
    user_input = input("Enter the value ")
    if user_input == "Exit":
        break
    total += int(user_input)
print(total)