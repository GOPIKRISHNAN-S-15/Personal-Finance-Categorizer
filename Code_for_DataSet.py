import pandas as pd
import random
categories = {
    "Food": ["McDonalds", "KFC", "Starbucks", "Dominos", "Subway"],
    "Clothing": ["Nike", "Adidas", "H&M", "Zara", "Levis"],
    "Electronics": ["Apple", "Samsung", "Sony", "Dell", "HP"],
    "Transport": ["Uber", "Lyft", "Ola", "RedBus", "Metro"],
    "Entertainment": ["Netflix", "Spotify", "Disney+", "YouTube Premium", "Amazon Prime"],
    "Grocery": ["Walmart", "Target", "Costco", "Tesco", "BigBazaar"]
}
payment_methods = ["Credit Card", "Debit Card", "UPI", "Cash", "Net Banking"]
locations = ["New York", "Los Angeles", "Chicago", "Houston", "San Francisco", "Boston"]
account_types = ["Savings", "Current", "Salary", "Credit Card"]
transaction_types = ["Debit", "Credit"]
device_used = ["Mobile", "Desktop", "ATM", "POS Terminal"]
merchant_types = ["Retail", "Restaurant", "Online Store", "Service", "Subscription"]
loyalty_program = ["Yes", "No"]
rows = []
for i in range(5000):
    category = random.choice(list(categories.keys()))
    brand = random.choice(categories[category])
    amount = round(random.uniform(5, 5000), 2)
    date = pd.to_datetime("2025-01-01") + pd.to_timedelta(random.randint(0, 364), unit="D")
    payment = random.choice(payment_methods)
    location = random.choice(locations)
    account = random.choice(account_types)
    txn_type = random.choice(transaction_types)
    device = random.choice(device_used)
    currency = "INR"  # Fixed currency
    merchant = random.choice(merchant_types)
    loyalty = random.choice(loyalty_program)
    weekday = date.strftime("%A")
    month = date.strftime("%B")
    time_of_day = random.choice(["Morning", "Afternoon", "Evening", "Night"])
    description = f"Transaction at {brand}"  # ADD "Transaction at " before brand
    rows.append([
        date.strftime("%Y-%m-%d"),
        description,
        amount,
        category,
        payment,
        location,
        account,
        txn_type,
        device,
        currency,
        merchant,
        loyalty,
        weekday,
        month,
        time_of_day
    ])
df = pd.DataFrame(rows, columns=[
    "Date", "Description", "Amount", "Category", "PaymentMethod",
    "Location", "AccountType", "TransactionType", "DeviceUsed",
    "Currency", "MerchantType", "LoyaltyProgram", "Weekday", "Month", "TimeOfDay"
])
df.to_csv("personal_finance_transactions_5000_INR.csv", index=False)
print("Mega feature-rich dataset with all currencies as INR generated successfully!")
