import os
import csv


with open("expenses.csv", "w") as file:
    writer = csv.DictWriter(file, fieldnames=["item", "price", "category"])
    writer.writeheader()
    print("File created successfully")


        