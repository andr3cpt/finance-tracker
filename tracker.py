import os
import csv

# Declare initial constant variables
FILE_NAME = "expenses.csv"
HEADERS = ["item", "category", "price",]

# Check if file exists; if not, create it
if not os.path.exists(FILE_NAME):
    print(f"Creating '{FILE_NAME}'...")
    with open(FILE_NAME, "w") as file:
        writer = csv.DictWriter(file, fieldnames=HEADERS)
        # Create the headers for each 'column'
        writer.writeheader()
        print(f"File: {FILE_NAME} created successfully.")
else:
    print(f"File: {FILE_NAME} ready.")

# Prompt user for 'item' and 'category'
item = input("Item: ")
category = input("Category: ")

# Use while loop to ask for 'price'; if not valid, re-prompt
while True:
    try:
        price = float(input("Price: "))
        break
    except ValueError:
        print("Invalid. Please enter a valid number: ")

# Open 'expenses.csv' in "a" mode ("append")
with open(FILE_NAME, "a") as file:
    writer = csv.DictWriter(file, fieldnames=HEADERS)
    # Write new data as a dictionary row
    writer.writerow({"item": item, "category": category, "price": price})

print("-- Expense saved successfully! --")
 
# Initialize container
expenses = []

# Access data 
with open(FILE_NAME, "r") as file:
    reader = csv.DictReader(file)
    # Loop through every row
    for row in reader:
        # Convert "price" to float
        row["price"] = float(row["price"])
        # Append to "expenses" list
        expenses.append(row)

# Sort list by prices (from highest to lowest)
sorted_expenses = sorted(expenses, key=lambda expense: expense["price"], reverse=True)

# Create "total" variable and set it to 0
total = 0

# Loop through sorted list
for expense in sorted_expenses:
    # Add current price to total
    total = total + expense["price"]
    # Print item, category and price
    print(f"Item: {expense['item']} | Category: {expense['category']} | Price: ${expense['price']}") # Moved "$" to the end to keep initial data "clean"
# Print total
print(f"TOTAL: ${total}")

