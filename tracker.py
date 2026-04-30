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

# --- To do ---
# 1. Prompt user for 'item' and 'category' (they're both strings)
# 2. Use while loop to ask for 'price'
# 3. Try: parse price as float() --> if succesful: break
# 4. Except: ValueError --> print("Not valid!") --> re-prompt user
# 4. Open 'expenses.csv' in "a" mode ("append")
# 5. Write new data as a dictionary row ("item": item, "price": price, "category": category)


        