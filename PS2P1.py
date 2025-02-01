stock_ticker = input("Enter the stock ticker symbol (e.g., TSLA): ")
num_shares = int(input("Enter the number of shares: "))
cost_per_share = float(input("Enter the cost per share: "))

amount_invested = num_shares * cost_per_share

print(f"The amount invested in {stock_ticker} is: ${amount_invested:.2f}")