print("--- Exercise 2---")
import csv

with open("data/sales.csv", mode="r") as file:
    reader = csv.reader(file)
    for row in reader:
        print(row)

print("--- Exercise 3---")
with open("data/sales.csv", mode="r") as file:
    reader = csv.reader(file)
    header = next(reader)
    print("Header:", header)

    for row in reader:
        print(row)

print("--- Exercise 4---")
total_revenue = 0
with open("data/sales.csv", mode="r") as file:
    reader = csv.reader(file)
    next(reader)

    for row in reader:
        product = row[0]
        price = float(row[1])
        quantity = int(row[2])

        revenue = price * quantity
        total_revenue += revenue

        print(f"{product}: {quantity} units x ${price:.2f} = ${revenue:.2f}")

    print(f"Total revenue across all rows: ${total_revenue:.2f}")

print("--- Exercise 5---")
rows_written = 0 
rows_original = 0

with open("data/sales.csv", mode="r") as infile, open("data/cleaned.csv", mode="w", newline="") as outfile:
    reader = csv.reader(infile)
    writer = csv.writer(outfile)
    
    header = next(reader)

    writer.writerow(["Product", "Price", "Quantity", "Total"])

    for row in reader:
        rows_original += 1
        product = row[0]
        price = float(row[1])
        quantity = int(row[2])
        revenue = price * quantity

        if revenue > 100:
            writer.writerow([product, price, quantity, revenue])
            rows_written += 1

            print(f"Rows written to cleaned.csv: {rows_written} vs {rows_original}")

print("--- Exercise 6---")
total_revenue_dict = 0
with open("data/sales.csv", mode="r") as file:
    reader = csv.DictReader(file)
    for row in reader:
        product = row["product"]
        price = float(row["price"])
        quantity = int(row["quantity"])
        total_revenue_dict += price * quantity

print(f"DictReader Total Revenue: ${total_revenue_dict:.2f}")

print("---Exercise 7---")
product_summary = {}

with open("data/sales.csv", mode="r") as file:
    reader = csv.DictReader(file)
    for row in reader:
        product = row["product"]
        revenue = float(row["price"]) * int(row["quantity"])

        if product in product_summary:
            product_summary[product] += revenue
        else:
            product_summary[product] = revenue

    for prod in sorted(product_summary.keys()):
        print(f"{prod}: ${product_summary[prod]:.2f}")


print("---Exercise 8---")
from datetime import datetime

log_revenue = 0 
with open("data/sales.csv", mode="r") as file:
    reader = csv.DictReader(file)
    for row in reader:
        log_revenue += float(row["price"]) * int(row["quantity"])

    current_time = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    log_line = f"{current_time} - Total revenue = ${log_revenue:.2f}\n"
    with open("data/sales_log.txt", mode="a") as log_file:
        log_file.write(log_line)

    print(f"Logged run: {log_line.strip()}")




    # Reflection

    # Q1
    #Python excels at automating repetitive pipelines,
    # handling massive datasets without slowing down,
    # and integrating with version control, whereas 
    # Excel provides immediate visual feedback, interactive 
    # ad-hoc filtering, and a much lower barrier to
    # entry for non-technical users.

    #Q2
    #An automated e-commerce inventory sync or order-fulfillment
    #tracker benefits greatly from append-mode logs because it records
    # continuous, chronological timestamps and status updates of every background
    #run without overwriting past audit data.
    
