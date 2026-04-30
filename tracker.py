import os
import csv

FILE_NAME = "expenses.csv"
HEADERS = ["item", "price", "category"]

if not os.path.exists(FILE_NAME):
    print(f"Creating '{FILE_NAME}'...")
    with open(FILE_NAME, "w") as file:
        writer = csv.DictWriter(file, fieldnames=HEADERS)
        writer.writeheader()
        print(f"File: {FILE_NAME} created successfully.")
else:
    print(f"File: {FILE_NAME} not found.")


        