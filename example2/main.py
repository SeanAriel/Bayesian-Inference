"""
For normally distributed data with known variance,
we can use conjugate priors for the mean, which also follows a normal distribution.
"""
import numpy as np
import matplotlib.pyplot as plt
from scipy.stats import norm

# Prior parameters
mu_0 = 15
sigma_0_squared = 4
sigma_0 = np.sqrt(sigma_0_squared)

# Known variance of the observations
sigma_squared = 4
sigma = np.sqrt(sigma_squared)

# Data (observations)
observations = [13, 14, 15, 16, 14]
n = len(observations)

# Sum of observations
sum_observations = sum(observations)

# Posterior parameters
mu_n = ((mu_0 / sigma_0_squared) + (sum_observations / sigma_squared)) / ((1 / sigma_0_squared) + (n / sigma_squared))
sigma_n_squared = 1 / ((1 / sigma_0_squared) + (n / sigma_squared))
sigma_n = np.sqrt(sigma_n_squared)

# Define the prior and posterior distributions
x = np.linspace(10, 20, 100)
prior = norm.pdf(x, mu_0, sigma_0)
posterior = norm.pdf(x, mu_n, sigma_n)

# Plot the prior and posterior distributions
plt.figure(figsize=(10, 5))
plt.plot(x, prior, label='Prior: N(15, 4)', linestyle='--')
plt.plot(x, posterior, label=f'Posterior: N({mu_n:.2f}, {sigma_n_squared:.2f})', linestyle='-')
plt.fill_between(x, posterior, alpha=0.5)
plt.title('Prior and Posterior Distributions')
plt.xlabel('Mean Arrival Time')
plt.ylabel('Density')
plt.legend()
plt.savefig('example2/prior_posterior_distributions.png')
plt.show()
