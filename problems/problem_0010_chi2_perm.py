"""
# Task 6 — Permutation Chi-Square Test

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
    observed = cont_table.values.astype(float)   # shape (2, k)
    row_sums = observed.sum(axis=1, keepdims=True)
    col_sums = observed.sum(axis=0, keepdims=True)
    total = observed.sum()

    # Expected counts under independence: E[i,j] = row_i_total * col_j_total / N
    expected = row_sums @ col_sums / total

    # Chi-square statistic: Σ (O - E)² / E, summed over all cells
    chi2_observed = float(((observed - expected) ** 2 / expected).sum())

    # --- Permutation null distribution ---
    # col_totals: number of visits per design (fixed across permutations)
    # total_clicks: total clicks in the whole table (fixed across permutations)
    col_totals = col_sums.flatten().astype(int)
    total_clicks = int(row_sums[0, 0])

    rng = np.random.default_rng(seed)
    chi2_random_values = np.empty(num_permutations)

    for i in range(num_permutations):
        # Draw a random allocation of clicks across groups (without replacement)
        perm_clicks = rng.multivariate_hypergeometric(col_totals, total_clicks).astype(float)
        perm_nonclicks = col_totals - perm_clicks
        perm_obs = np.vstack([perm_clicks, perm_nonclicks])

        perm_row_sums = perm_obs.sum(axis=1, keepdims=True)
        perm_col_sums = perm_obs.sum(axis=0, keepdims=True)
        perm_expected = perm_row_sums @ perm_col_sums / total

        chi2_random_values[i] = ((perm_obs - perm_expected) ** 2 / perm_expected).sum()

    # p-value = P(chi2_null ≥ chi2_observed) estimated from the permutation distribution
    p_value = float(np.mean(chi2_random_values >= chi2_observed))

    return {
        "expected": expected,
        "chi2_observed": chi2_observed,
        "chi2_random_mean": float(chi2_random_values.mean()),
        "p_value": p_value,
        "are_clicks_different": p_value < 0.05,
    }

pytest_cases = [
    (pd.DataFrame({'Design A': [115, 9885], 'Design B': [150, 9850], 'Design C': [130, 9870]}),
     {'are_clicks_different': False}),  # p-value should be > 0.05, no significant difference
    (pd.DataFrame({'Design A': [200, 9800], 'Design B': [150, 9850], 'Design C': [100, 9900]}),
     {'are_clicks_different': True}),   # p-value should be < 0.05, significant difference
]
@pytest.mark.parametrize("cont_table, expected", pytest_cases)
def test_chi2_perm_test(cont_table, expected):
    result = chi2_perm_test(cont_table)
    assert result['are_clicks_different'] == expected['are_clicks_different']
    assert 'expected' in result
    assert 'chi2_observed' in result
    assert 'chi2_random_mean' in result
    assert 'p_value' in result  