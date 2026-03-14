import numpy as np
import matplotlib.pyplot as plt

initial_investment = 1000
average_return = 0.07
volatility = 0.15
years = 30
simulations = 1000

final_values = []

for i in range(simulations):

    value = initial_investment

    for year in range(years):
        random_return = np.random.normal(average_return, volatility)
        value = value * (1 + random_return)

    final_values.append(value)

print("Average outcome:", np.mean(final_values))
print("Best outcome:", np.max(final_values))
print("Worst outcome:", np.min(final_values))
print("Probability of loss:", np.mean(np.array(final_values) < initial_investment))
plt.hist(final_values, bins=50)
plt.xlabel("Final Investment Value")
plt.ylabel("Frequency")
plt.title("Monte Carlo Simulation")
plt.show()