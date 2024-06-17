"""
We'll use the Beta-Binomial conjugacy property,
which allows us to update the Beta prior with Binomial likelihood in a straightforward way.
"""
import numpy as np
import matplotlib.pyplot as plt
from scipy.stats import beta

# Prior parameters
alpha_prior = 2
beta_prior = 2

# Data
successes = 8
trials = 10

# Posterior parameters
alpha_post = alpha_prior + successes
beta_post = beta_prior + trials - successes

# Define the prior, likelihood, and posterior distributions
x = np.linspace(0, 1, 100)
prior = beta.pdf(x, alpha_prior, beta_prior)
posterior = beta.pdf(x, alpha_post, beta_post)

# Plot the prior and posterior distributions
plt.figure(figsize=(10, 5))
plt.plot(x, prior, label='Prior: Beta(2, 2)', linestyle='--')
plt.plot(x, posterior, label='Posterior: Beta(10, 4)', linestyle='-')
plt.fill_between(x, posterior, alpha=0.5)
plt.title('Prior and Posterior Distributions')
plt.xlabel('Probability of Success')
plt.ylabel('Density')
plt.legend()
plt.savefig('example1/prior_posterior_distributions.png')
plt.show()
