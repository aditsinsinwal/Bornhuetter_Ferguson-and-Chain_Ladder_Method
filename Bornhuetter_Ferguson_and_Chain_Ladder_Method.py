# -*- coding: utf-8 -*-
import numpy as np

def chain_ladder_method(claims_data):

    num_accident_years = claims_data.shape[1]
    num_development_years = claims_data.shape[0]

    estimated_future_claims = np.zeros(num_accident_years)

    for i in range(num_accident_years - 1):
        for j in range(num_development_years - i - 1):
            development_factor = claims_data[j + 1, i] / claims_data[j, i]
            estimated_future_claims[i] += development_factor * claims_data[-1, i]

    return estimated_future_claims

# Example usage:
claims_data = np.array([
    [1000, 2000, 3000],
    [1500, 2500, 0],
    [1800, 0, 0],
    [0, 0, 0]  # Latest development year (current year)
])

estimated_claims = chain_ladder_method(claims_data)
print("Estimated future claims:", estimated_claims)

def bornhuetter_ferguson(incurred_losses, development_factors):

    num_development_years = len(incurred_losses)
    ultimate_losses = np.zeros(num_development_years)

    for i in range(num_development_years):
        factor_sum = np.sum(development_factors[i:])
        ultimate_losses[i] = incurred_losses[i] + (factor_sum * incurred_losses[i])

    return ultimate_losses

# Example usage:
incurred_losses = np.array([1000, 2000, 3000, 4000])
development_factors = np.array([0.7, 0.8, 0.85, 0.9])

estimated_ultimate_losses = bornhuetter_ferguson(incurred_losses, development_factors)
print("Estimated ultimate losses:", estimated_ultimate_losses)
