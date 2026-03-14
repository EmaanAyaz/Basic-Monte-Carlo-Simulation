# Basic-Monte-Carlo-Simulation


## Overview
Monte Carlo simulation in Python modelling long-term investment outcomes under uncertainty. Simulates 1000 independent investment outcomes using normally distributed annual returns (7% mean, 15% volatility) over 30 years, analysing the distribution of final portfolio values and the probability of loss.

---

## Project Description
This project implements a Monte Carlo simulation to model long-term investment growth under uncertain market conditions.

Random annual returns are generated from a normal distribution and compounded over a 30-year investment horizon. By repeating this process across 1000 simulations, the model produces a distribution of possible final portfolio values.

The simulation demonstrates how volatility, compounding, and randomness influence long-term investment outcomes.

---

## Model Assumptions

| Parameter | Value |
|----------|------|
| Initial Investment | £1000 |
| Expected Annual Return | 7% |
| Volatility (Standard Deviation) | 15% |
| Investment Horizon | 30 years |
| Simulations | 1000 |

These assumptions roughly approximate the behaviour of long-term equity markets.

---

## Key Outputs

The simulation calculates:

- Average final portfolio value  
- Best and worst simulated outcomes  
- Probability of loss after 30 years  
- Distribution of final investment values

A histogram is generated to visualise the probability distribution of results.

---

## Libraries Used

- **NumPy** – numerical computing and random sampling
- **Matplotlib** – data visualisation and plotting

---

## Concepts Demonstrated

- Monte Carlo simulation
- Stochastic modelling
- Compound investment returns
- Probability distributions in finance
- Risk analysis under uncertainty

---

## Possible Extensions

Potential improvements to the model include:

- Using historical market data
- Modelling market crashes or fat-tailed distributions
- Simulating multi-asset portfolios
- Increasing the number of simulations



