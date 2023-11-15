# Monte Carlo Stock Predictor
Shopify stock predictor using Monte Carlo simulation

Monte Carlo simulations provide a visual and statistical tool to assess potential stock price
movements, incorporating both historical returns and inherent volatility.

Modify 'threshold' variable on line 30 to see the likelihood of Shopify stock exceeding the given amount in the next year.

Simulation runs for 252 trading days.

Data is obtained from Yahoo Finance as of 2023/10/15

![Stock prediction chart](SHOP.png)

**Findings:**

**Initial Price: $51.55** The starting point for our simulations was the stock's most recent price of $51.55. This value
serves as the foundation upon which the simulated price paths are built, using the mean and
standard deviation values as guiding metrics.

**Mean of Daily Return:** Based on the Shopify stock price historical data, the mean daily
return was calculated to be approximately 0.24%.
This indicates that, on average, the stock has increased by 0.24% every trading day based on the
historical data provided. It's a representation of the expected daily price change. While this might
seem small on a day-to-day basis, over a more extended period, such consistent gains could
compound into significant returns.

**Standard Deviation of Daily Return:** The standard deviation, which indicates volatility or
risk, was found to be around 3.92%.
ML Assignment 4: Monte Carlo Simulation 4
The standard deviation measures the stock's volatility or how much the stock's returns can
deviate from its average return. A higher standard deviation indicates more volatility and, thus,
potentially more risk. In this case, the stock's returns can deviate by approximately 3.92% daily.
It means that even though the average return is 0.24%, the stock price can potentially go up or
down by 3.92% (or even more, though less likely) on any given day.

**Probability of Exceeding Threshold:** By running the simulation 10,000 times, it was
determined that the stock price exceeds a specific threshold (set by the user) with a
probability of XX% within the next year. (Note: XX% is a placeholder and needs to be
replaced with the actual value derived from the simulation.) In this assignment, the threshold
is $200.

**Probability of Stock Price Exceeding $200 in the Next Year: 9.49%**
After running 10,000 simulations, it was observed that in 9.49% of those scenarios, the stock
price exceeded the $200 mark at some point within the year. This doesn't mean the stock will
necessarily close above $200 by the end of the year, but it suggests there's nearly a 1 in 10
chance of the stock price touching or crossing the $200 threshold based on historical volatility
and return patterns.


**Noted: z = np.random.normal(0, 1) :**
This line generates random numbers from a standard normal distribution. Because of this
randomness, the simulated stock price paths will be different each time you run the code. This
will result in a different visual output (plot) every time.
* Purpose: This generates a single random number sampled from a standard normal
  distribution (mean = 0, standard deviation = 1).
* When to use: This is used in your Monte Carlo simulation to introduce randomness,
  simulating the inherent uncertainty in the stock market movements based on the geometric
  Brownian motion.
