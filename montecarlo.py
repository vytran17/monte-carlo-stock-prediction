import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

df = pd.read_csv("SHOP.csv", parse_dates=["Date"])

# Calculate daily percentage change in the "Close" column
# and stores it in a new column called 'Daily Return'.
df["Daily Return"] = df["Close"].pct_change()

# Calculate mean and standard deviation of the daily return
mean_return = df["Daily Return"].mean()
std_return = df["Daily Return"].std()

# Print results in percentage format
print(f"Mean of Daily Return: {mean_return * 100:.2f}%")
print(f"Standard Deviation of Daily Return: {std_return * 100:.2f}%")

# Monte Carlo simulation to forecast stock prices using the
# geometric Brownian motion model

# Last known stock price - the stock price at time t
S_t = df["Close"].iloc[-1]  
mu = mean_return
sigma = std_return
# Approximate number of trading days in a year
days = 252  
num_simulations = 10000
# The desired threshold value. Current price is 51.55 USD
threshold = 200  
print(f"The initial price is: {S_t}$")

exceeded_threshold_count = 0

plt.figure(figsize=(10, 6))

# a loop to run the Monte Carlo simulation num_simulations times.
for i in range(num_simulations):  
    prices = [S_t]
    # inner loop runs days times to simulate stock prices
    # using the geometric Brownian motion formula
    for _ in range(days):
        z = np.random.normal(0, 1)
        S_t1 = prices[-1] * np.exp((mu - sigma**2 / 2) + sigma * z)
        prices.append(S_t1)

    # Check if stock price exceeds threshold in this simulation
    if any(price > threshold for price in prices):
        exceeded_threshold_count += 1

    # Plot only the first 40 paths for visualization
    if i < 40:
        plt.plot(prices, label=f"Simulation {i+1}")

probability = exceeded_threshold_count / num_simulations
print(
    f"Probability of stock price exceeding {threshold} in the next year: {probability*100:.2f}"
)

# Customize the plot
plt.title("Simulated SHOPIFY Stock Price Paths")
plt.xlabel("Trading Days")
plt.ylabel("Stock Price in $")
plt.grid(True)
plt.show()
