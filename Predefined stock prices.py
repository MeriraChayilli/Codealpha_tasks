
stock_prices = {
    "AAPL": 180,
    "TSLA": 250,
    "GOOG": 2700,
    "MSFT": 300,
    "AMZN": 3300
}

total_investment = 0

print("Stock Portfolio Tracker")
print("Available stocks:", ", ".join(stock_prices.keys()))

while True:
    stock_name = input("Enter stock name (or 'done' to finish): ").upper()
    
    if stock_name == "DONE":
        break
    
    if stock_name not in stock_prices:
        print("Stock not found. Please try again.")
        continue
    
    quantity = int(input(f"Enter quantity for {stock_name}: "))
    
    price = stock_prices[stock_name]
    investment = price * quantity
    total_investment += investment
    
    print(f"Added {stock_name} - Investment: {investment}")

print("\nTotal Investment Value:", total_investment)

# Save result to file (optional)
with open("portfolio.txt", "w") as file:
    file.write(f"Total Investment Value: {total_investment}")

print("Portfolio saved to 'portfolio.txt'")