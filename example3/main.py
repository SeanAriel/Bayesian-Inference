"""
For Gamma-Poisson conjugate priors,
the posterior distribution of the rate parameter λ of the Poisson distribution is also Gamma-distributed.
"""
import numpy as np
import matplotlib.pyplot as plt
from scipy.stats import gamma

# Prior parameters
alpha_prior = 2
beta_prior = 1

# Data (observations)
defective_items = [3, 4, 2, 5]
n = len(defective_items)

# Sum of observations
sum_defective = sum(defective_items)

# Posterior parameters
alpha_post = alpha_prior + sum_defective
beta_post = beta_prior + n

# Define the prior and posterior distributions
x = np.linspace(0, 10, 100)
prior = gamma.pdf(x, alpha_prior, scale=1/beta_prior)
posterior = gamma.pdf(x, alpha_post, scale=1/beta_post)

# Plot the prior and posterior distributions
plt.figure(figsize=(10, 5))
plt.plot(x, prior, label='Prior: Gamma(2, 1)', linestyle='--')
plt.plot(x, posterior, label=f'Posterior: Gamma({alpha_post}, {1/beta_post:.2f})', linestyle='-')
plt.fill_between(x, posterior, alpha=0.5)
plt.title('Prior and Posterior Distributions')
plt.xlabel('Defect Rate per Hour')
plt.ylabel('Density')
plt.legend()
plt.savefig('example3/prior_posterior_distributions.png')  # Save the figure
plt.show()
