# Stock Portfolio Tracker

# Hardcoded stock prices
stock_prices = {
    "AAPL": 180,
    "TSLA": 250,
    "GOOGL": 140,
    "MSFT": 420,
    "AMZN": 190
}

portfolio = {}
total_investment = 0

print("=" * 40)
print("      STOCK PORTFOLIO TRACKER")
print("=" * 40)

while True:
    print("\nAvailable Stocks:")
    for stock, price in stock_prices.items():
        print(f"{stock} : ${price}")

    stock_name = input("\nEnter stock symbol (or 'done' to finish): ").upper()

    if stock_name == "DONE":
        break

    if stock_name not in stock_prices:
        print("❌ Invalid stock symbol. Please choose from the list.")
        continue

    try:
        quantity = int(input(f"Enter quantity of {stock_name}: "))

        if quantity <= 0:
            print("❌ Quantity must be greater than 0.")
            continue

        if stock_name in portfolio:
            portfolio[stock_name] += quantity
        else:
            portfolio[stock_name] = quantity

    except ValueError:
        print("❌ Please enter a valid integer quantity.")

# Calculate total investment
print("\n" + "=" * 40)
print("         PORTFOLIO SUMMARY")
print("=" * 40)

for stock, quantity in portfolio.items():
    price = stock_prices[stock]
    investment = price * quantity
    total_investment += investment

    print(f"{stock:<10} Qty: {quantity:<5} "
          f"Price: ${price:<5} Value: ${investment}")

print("-" * 40)
print(f"TOTAL INVESTMENT VALUE: ${total_investment}")
print("=" * 40)

# Save results to a text file
with open("portfolio_report.txt", "w") as file:
    file.write("STOCK PORTFOLIO REPORT\n")
    file.write("=" * 40 + "\n")

    for stock, quantity in portfolio.items():
        price = stock_prices[stock]
        investment = price * quantity

        file.write(
            f"{stock} | Quantity: {quantity} | "
            f"Price: ${price} | Value: ${investment}\n"
        )

    file.write("-" * 40 + "\n")
    file.write(f"TOTAL INVESTMENT VALUE: ${total_investment}\n")

print("\n✅ Portfolio report saved as 'portfolio_report.txt'")