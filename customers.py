print("--- Exercise 1 ---")
customer = {
    "name": "Alice",
    "Name": "Not-Alice",
    "email": "alice@example.com",
    "tier": "gold",
    "ytd_spend": 12400,
}

print(customer["name"])  # Accessing the value associated with the key "name"
print(customer["email"])  # Accessing the value associated with the key "email"
print(customer["tier"])  # Accessing the value associated with the key "tier"
print(customer["ytd_spend"])  # Accessing the value associated with the key "ytd_spend"


print("--- Exercise 2 ---")
customer['phone'] = '555-5555'
print(customer)
customer['tier'] = 'platinum'
print(customer)
del customer['Name']
print(customer)

print(customer.get('ytd_spend',0))

print("--- Exercise 3 ---")
print(customer.get("email", "no email on file"))

#try:
#    print(customer["email"])
#except KeyError as error:
#    print(f"KeyError caught: {error}")

print("--- Exercise 4 ---")
for key, value in customer.items():
    print(f"{key}: {value}")

for key in customer:
    print(key, customer[key])

print("--- Exercise 5 ---")
tier_discounts = {"bronze": 0, "silver": 0.05, "gold": 0.1, "platinum": 0.15}

purchase = 200
discount_rate = tier_discounts.get(customer["tier"], 0)
final_price = purchase * (1 - discount_rate)
print(f"Tier: {customer['tier']}")
print(f"Discount Rate: {discount_rate * 100}%")
print(f"Final Price: ${final_price:.2f}")

print("--- Exercise 6 ---")
customers = [
    {"name": "Bob", "tier": "silver", "ytd_spend": 3200},
    {"name": "Carol", "tier": "gold", "ytd_spend": 8750},
    {"name": "David", "tier": "bronze", "ytd_spend": 450},
]

for record in customers:
    rate = tier_discounts.get(record["tier"], 0)
    discount = 300 * rate
    print(f"{record['name']} ({record['tier']}): ${discount:.2f} off a $300 purchase")

print("--- Exercise 7 ---")
catalog = {
    "Widget A": {"price": 9.99, "stock": 150},
    "Gadget C": {"price": 49.99, "stock": 8},
}
for name, details in catalog.items():
    if details["stock"] < 20:
        print(f"LOW STOCK: {name} - only {details['stock']} left")

print("--- Exercise 8 ---")
transactions = [
    {"region": "South", "amount": 300},
    {"region": "North", "amount": 150},
    {"region": "South", "amount": 200},

]

sales_by_region = {}
for sale in transactions:
    region = sale["region"]
    amount = sale["amount"]
    sales_by_region[region] = sales_by_region.get(region, 0) + amount

print(sales_by_region)

for region in sorted(sales_by_region):
    print(f"{region}: ${sales_by_region[region]:.2f}")

# Questions
# 1. I'd use .get() whenever a missing key is a normal possibility, like optional
#    fields in customer records (not everyone has a phone or email on file). It
#    lets the program keep running with a sensible default instead of crashing.
#    I'd use bracket notation when the key must exist, like a customer's name or ID,
#    because if it's missing something is actually wrong and I want the error to
#    show up right away. My rule of thumb is if missing is okay, use .get(); if
#    missing is a bug, use brackets.
# 2. This pattern is basically a SUMIF or a pivot table in Excel, where you group
#    rows by a category like region and total up the amounts. The Python version
#    scales better because it can handle millions of rows without slowing down or
#    hitting spreadsheet limits. It's also repeatable, so I can rerun the same
#    script on new data every month instead of rebuilding formulas by hand.