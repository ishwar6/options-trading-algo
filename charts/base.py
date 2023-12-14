import matplotlib.pyplot as plt
import numpy as np

# Buy 21350 Call 21 Dec 2023: This is a long call option where you have the right, 
# but not the obligation, to buy the NIFTY 50 index at 21,350 points any time before the expiration date on 21 December 2023. 
# For this right, you pay a premium of 99.60 per share, and since one lot consists of 50 shares, the total premium paid is 99.60 x 50.

# Sell 21400 Call 21 Dec 2023: This is a short call option where you sell someone else the right to buy the NIFTY 50 index from you at 21,400 points before 21 December 2023. 
# For selling this option, you receive a premium of 77.00 per share, totaling 77.00 x 50 for one lot.

                                                                                      
# Define the parameters
buy_call_strike = 21350
sell_call_strike = 21400

premium_buy = 99.60
premium_sell = 77.00

nifty_prices = np.linspace(21000, 21600, 400)
one_lot_shares = 50

# Calculate the payoffs
buy_call_payoff = np.maximum(nifty_prices - buy_call_strike, 0) - premium_buy
sell_call_payoff = premium_sell - np.maximum(nifty_prices - sell_call_strike, 0)
net_payoff = (buy_call_payoff + sell_call_payoff) * one_lot_shares

# Calculate break-even point (where net_payoff is 0)
break_even = buy_call_strike + (premium_buy - premium_sell)

# Plot the graph
plt.figure(figsize=(10, 6))
plt.plot(nifty_prices, buy_call_payoff * one_lot_shares, label='Long 21350 Call Payoff', color='blue')
plt.plot(nifty_prices, sell_call_payoff * one_lot_shares, label='Short 21400 Call Payoff', color='orange')
plt.plot(nifty_prices, net_payoff, label='Net Payoff', color='green')
plt.axhline(0, color='black', lw=0.5)
plt.axvline(x=buy_call_strike, color='grey', linestyle='--', lw=0.5)
plt.axvline(x=sell_call_strike, color='grey', linestyle='--', lw=0.5)
plt.axvline(x=break_even, color='red', linestyle='--', lw=0.5, label='Break-even Point')
plt.title('Bull Call Spread Payoff Diagram')
plt.xlabel('NIFTY Index Level')
plt.ylabel('Profit / Loss')
plt.legend()
plt.grid(True)
plt.show()


