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
category = input("Category (e.g. food, tech, transport): ")

# Use while loop to ask for 'price'; if not valid, re-prompt
while True:
    try:
        price= float(input("Price: "))
        break
    except ValueError:
        print("Invalid. Please enter a valid number: ")

# Open 'expenses.csv' in "a" mode ("append")
with open(FILE_NAME, "a") as file:
    writer = csv.DictWriter(file, fieldnames=HEADERS)
    # Write new data as a dictionary row
    writer.writerow({"item": item, "category": category, "price": f"${price}"}) # f-string to add '$' sign

print("-- Expense saved successfully! --")
 
