import os
import csv


if not os.path.exists("expenses.csv"):
    print("Creating 'expenses.csv'...")
    with open("expenses.csv", "w") as file:
        writer = csv.DictWriter(file, fieldnames=["item", "price", "category"])
        writer.writeheader()
        print("File created successfully")
else:
    print("File: 'expenses.csv' not found.")


        