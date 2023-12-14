# In options trading, the premium is the cost of the potential opportunity to benefit from price movements without the obligation to buy. 
# It's important to remember that the premium paid is a sunk cost — once paid, it's not recoverable, 
# so it must be considered when calculating the total profit or loss of the options trade.


# Python function that calculates the profit or loss from an options trade

def calculate_options_profit(market_price, strike_price, premium_paid, contract_size=1, lot_size=50):
    """
    Calculate the profit or loss of a call option trade.
    
    :param market_price: The market price of the underlying asset
    :param strike_price: The strike price of the option
    :param premium_paid: The premium paid per share for the option
    :param contract_size: The number of contracts traded (default is 1)
    :param lot_size: The number of shares per contract (default is 50)
    :return: Total profit or loss from the trade
    """
    # Calculate profit from the trade if the option is exercised
    profit_from_exercise = max(market_price - strike_price, 0) * contract_size * lot_size
    
    # Calculate the total premium paid for the option
    total_premium_paid = premium_paid * contract_size * lot_size
    
    # Calculate the total profit or loss
    total_profit_or_loss = profit_from_exercise - total_premium_paid
    
    return total_profit_or_loss

# IJs scenario
market_price = 214  # The market price of the ticket (or NIFTY index level)
strike_price = 213.50  # The strike price at which IJ has the right to buy
premium_paid = 99.60  # The premium paid per share for the option

# Calculate the profit or loss for IJ's trade
profit_or_loss = calculate_options_profit(market_price, strike_price, premium_paid)

print(profit_or_loss)

-4955.0
