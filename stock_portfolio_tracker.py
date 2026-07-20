# Stock Portfolio Tracker

stock_prices = {
    "AAPL": 180,
    "TSLA": 250,
    "GOOGL": 140,
    "MSFT": 330,
    "AMZN": 130
}

total_investment = 0

print("Available Stocks:")
for stock, price in stock_prices.items():
    print(stock, ":", "$", price)

n = int(input("\nEnter number of different stocks: "))

for i in range(n):
    stock = input("\nEnter stock name: ").upper()

    if stock in stock_prices:
        quantity = int(input("Enter quantity: "))
        investment = stock_prices[stock] * quantity
        total_investment += investment
        print("Investment in", stock, "=", "$", investment)
    else:
        print("Stock not available!")

print("\nTotal Investment =", "$", total_investment)

# Save result to text file
with open("portfolio.txt", "w") as file:
    file.write("Total Investment = $" + str(total_investment))

print("Result saved in portfolio.txt")