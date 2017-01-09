import math
import numpy as np

# Each item in this list represents one k, starting from 0 and going up to and including 30.
outcome_counts = list(range(31))


def find_probability(N, k, p, q):
    # Find the probability of any single combination.
    term_1 = p ** k
    term_2 = q ** (N - k)
    combo_prob = term_1 * term_2

    # Find the number of combinations.
    numerator = math.factorial(N)
    denominator = math.factorial(k) * math.factorial(N - k)
    combo_count = numerator / denominator

    return combo_prob * combo_count


outcome_probs = [find_probability(30, i, .39, .61) for i in outcome_counts]
print(np.asarray(outcome_probs))