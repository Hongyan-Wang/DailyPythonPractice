"""
# Permutation Chi-Square Test

## Background

Permutation testing is a modern, generic approach to testing statistical hypotheses. While traditional hypothesis testing is based on case-specific formulas and assumptions which don't always hold in practice, permutation testing provides a single, unified, non-parametric framework to perform all kinds of tests.

The idea is to randomly permute the data multiple times and calculate the quantity of interest each time. This way, we obtain the said quantity's distribution that captures variation that is produced by random chance. Then, we compare the quantity of interest we have observed in our data to the distribution of its random variation and calculate the p-value.

## Problem

The goal of this task is to write a function that applies permutation testing to perform a **chi-square test** in order to compare the click-through rates of three website designs.
 
Write a function:

```python
def chi2_perm_test(cont_table)
```

which should take one argument called `cont_table`. This is a **contingency table**: a pandas DataFrame with three columns (each corresponding to three different website designs) and two rows:
- The first row containing the number of clicks for each website design
- The second row specifying the number of user visits without a click

For example, in the following contingency table we have 10K user visits for each of the three website designs, and for the first one, 115 visits ended up with a click.

## Requirements

- Use permutation testing (1000 permutations) to generate a null distribution of chi-square statistics
- Calculate the observed chi-square statistic
- Calculate the p-value as the proportion of permuted chi-square values greater than the observed
- Return a dictionary with the following keys:
  - `"expected"` — expected click counts under the null hypothesis
  - `"chi2_observed"` — the observed chi-square statistic
  - `"chi2_random_mean"` — mean chi-square statistic from permutations
  - `"p_value"` — the p-value
  - `"are_clicks_different"` — `True` if `p_value < 0.05`, else `False`

## Imports Available

```python
import numpy as np
import pandas as pd
from random_clicks_generator import RandomClicksGenerator
```

> Note: `RandomClicksGenerator` is a helper class provided in the test environment with a `shuffled_clicks()` method for generating permuted samples.
"""
import pytest

import numpy as np
import pandas as pd
class RandomClicksGenerator:
    def __init__(self, num_ones: int, num_zeros: int):
        self.rng = np.random.default_rng(1984)
        self.clicks = np.array([1] * num_ones + [0] * num_zeros)

    def shuffled_clicks(self) -> np.ndarray:
        return self.rng.permutation(self.clicks)

def chi2_perm_test(cont_table, num_permutations=1000, seed=42):
    """
    Permutation chi-square test comparing click-through rates across website designs.

    Parameters
    ----------
    cont_table : pd.DataFrame, shape (2, k)
        Contingency table: row 0 = clicks, row 1 = non-clicks; one column per design.
    num_permutations : int
        Number of random permutations used to build the null distribution.
    seed : int
        Random seed for reproducibility.

    Returns
    -------
    dict with keys:
        expected           — expected click counts under H0 (independence)
        chi2_observed      — chi-square statistic on the real data
        chi2_random_mean   — mean chi-square over all permutations (null distribution centre)
        p_value            — proportion of permuted chi2 values ≥ chi2_observed
        are_clicks_different — True if p_value < 0.05

    Permutation logic
    -----------------
    Under H0 (designs have equal CTR), each user's click outcome (1 or 0) is
    independent of which design they saw.  A valid null sample therefore keeps
    the group sizes (column sums) fixed but randomly reassigns clicks across
    groups.  This is equivalent to drawing from a multivariate hypergeometric
    distribution: given N total users with K clicks spread across groups of
    sizes n1, n2, …, how many clicks fall in each group by pure chance?
    """

    observed = cont_table.values.astype(float)

    # Step 1: expected counts
    total = observed.sum()
    row_sum = observed.sum(axis=1, keepdims=True)
    col_sum = observed.sum(axis=0, keepdims=True)
    expected = row_sum @ col_sum / total

    # Step 2: observed chi-square
    chi2_observed = float(((observed - expected) ** 2 / expected).sum())

    # Step 3: initialize RandomClicksGenerator
    total_clicks = int(observed[0].sum())
    total_nonclicks = int(observed[1].sum())
    generator = RandomClicksGenerator(total_clicks, total_nonclicks)

    group_sizes = observed.sum(axis=0).astype(int)
    num_permutations = 1000
    chi2_random = np.empty(num_permutations)

    # Step 4: permutation loop
    for i in range(num_permutations):
        permuted = generator.shuffled_clicks()

        split1 = group_sizes[0]
        split2 = group_sizes[0] + group_sizes[1]

        group1 = permuted[:split1]
        group2 = permuted[split1:split2]
        group3 = permuted[split2:]

        perm_clicks = np.array([
            group1.sum(),
            group2.sum(),
            group3.sum()
        ], dtype=float)

        perm_nonclicks = group_sizes - perm_clicks

        perm_obs = np.vstack([perm_clicks, perm_nonclicks])

        perm_row_sum = perm_obs.sum(axis=1, keepdims=True)
        perm_col_sum = perm_obs.sum(axis=0, keepdims=True)
        perm_expected = perm_row_sum @ perm_col_sum / total

        chi2_random[i] = ((perm_obs - perm_expected) ** 2 / perm_expected).sum()

    # Step 5: p-value
    p_value = float(np.mean(chi2_random > chi2_observed))

    # Step 6: return result
    return {
        "expected": [int(expected[0, 0]), int(expected[1, 0])],
        "chi2_observed": chi2_observed,
        "chi2_random_mean": float(chi2_random.mean()),
        "p_value": p_value,
        "are_clicks_different": p_value < 0.05
    }



def test_chi2_perm_test_example_case():
    cont_table = pd.DataFrame([[115, 98, 123], [9885, 9902, 9877]])

    result = chi2_perm_test(cont_table)

    # Check keys
    assert set(result.keys()) == {
        "expected",
        "chi2_observed",
        "chi2_random_mean",
        "p_value",
        "are_clicks_different",
    }

    # Check types
    assert isinstance(result["expected"], list)
    assert len(result["expected"]) == 2
    assert all(isinstance(x, int) for x in result["expected"])

    assert isinstance(result["chi2_observed"], float)
    assert isinstance(result["chi2_random_mean"], float)
    assert isinstance(result["p_value"], float)
    assert isinstance(result["are_clicks_different"], bool)

    # Check exact / near-exact values from the example
    assert result["expected"] == [112, 9888]
    assert np.isclose(result["chi2_observed"], 2.943683541377716)
    assert np.isclose(result["chi2_random_mean"], 2.117844862459547)
    assert np.isclose(result["p_value"], 0.257)
    assert result["are_clicks_different"] is False