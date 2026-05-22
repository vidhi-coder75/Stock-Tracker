# Stock Portfolio Tracker

# Hardcoded stock prices
stock_prices = {
    "AAPL": 180,
    "TSLA": 250,
    "GOOGL": 140,
    "MSFT": 320
}

total_investment = 0

# User input
stock_name = input("Enter stock name (AAPL/TSLA/GOOGL/MSFT): ").upper()
quantity = int(input("Enter quantity: "))

# Check if stock exists
if stock_name in stock_prices:
    total_investment = stock_prices[stock_name] * quantity
    
    print("\nStock:", stock_name)
    print("Price per share:", stock_prices[stock_name])
    print("Quantity:", quantity)
    print("Total Investment Value:", total_investment)

    # Save result in a text file
    file = open("portfolio.txt", "w")
    file.write(f"Stock: {stock_name}\n")
    file.write(f"Quantity: {quantity}\n")
    file.write(f"Total Investment: {total_investment}\n")
    file.close()

    print("\nResult saved in portfolio.txt")

else:
    print("Stock not found!")