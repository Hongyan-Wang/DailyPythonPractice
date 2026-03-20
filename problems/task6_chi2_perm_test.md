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
