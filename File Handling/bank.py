
n = int(input("Enter number of transactions: "))
f = open("bank.txt", "w")

f.write("Type,Amount\n")
for i in range(n):
    transaction = input("Enter transaction (deposit/withdrawal): ")
    amount = float(input("Enter amount: "))

    f.write(transaction + "," + str(amount) + "\n")

f.close()

print("\nTransactions saved successfully!")

f = open("transactions.txt", "r")

records = f.readlines()

f.close()
records = records[1:]

total_deposits = 0
total_withdrawals = 0
largest = 0

for record in records:
    transaction, amount = record.strip().split(",")
    amount = float(amount)

    if transaction.lower() == "deposit":
        total_deposits = total_deposits + amount
    elif transaction.lower() == "withdrawal":
        total_withdrawals = total_withdrawals + amount

    if amount > largest:
        largest = amount

final_balance = total_deposits - total_withdrawals

print("\n--- Bank Summary ---")
print("Total Deposits:", total_deposits)
print("Total Withdrawals:", total_withdrawals)
print("Final Balance:", final_balance)
print("Largest Transaction:", largest)