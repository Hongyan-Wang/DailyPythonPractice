"""
# Task 4 — Check if Random Variables are Independent

## Problem

You are given a table `distr_table` with a joint probability distribution of two random variables X and Y, for example:

| X | Y | pr    |
|---|---|-------|
| 0 | 1 | 0.30  |
| 0 | 2 | 0.25  |
| 1 | 1 | 0.15  |
| 1 | 2 | 0.30  |

As you can see, for example P(X=0 ∧ Y=1) = 0.3, P(Y=1) = 0.3 + 0.15 = 0.45. Probabilities in the third column add up to 1.

Write a method `check_independence` that for a given `distr_table` returns a **dictionary of length 3**, where:

- **First element** (key named `are_independent`) is a boolean which states if X and Y are independent (`True`) or not (`False`).

  Two random variables are independent if for each possible value x for X and for each possible value y for Y:

  ```
  P(X = x ∧ Y = y) = P(X = x) * P(Y = y)
  ```

- **Second element** (key named `cov`) is a covariance between X and Y (i is an indicator of i-th of n possible pairs (xᵢ, yᵢ) of (X, Y)):

  ```
  Cov(X, Y) = Σ pᵢ(xᵢ − μₓ)(yᵢ − μᵧ)
  ```

  where:

  ```
  μₓ = Σ pⱼxⱼ,   μᵧ = Σ pₖyₖ
  ```

- **Third element** (key named `corr`) is a correlation coefficient between X and Y:

  ```
  corr(X, Y) = Cov(X, Y) / (σₓ · σᵧ)
  ```

  where:

  ```
  σₓ = sqrt( Σ pⱼ(xⱼ − μₓ)² ),   σᵧ = sqrt( Σ pₖ(yₖ − μᵧ)² )
  ```

  In the above equations m and l are numbers of unique values of X and Y respectively.

> **Note:** You cannot use built-in functions e.g. `cov` and `corrcoef` from the numpy package for points two and three since we use distributions, not samples, to describe variables X and Y.

Write a class:

```python
import numpy as np
import pandas as pd

class CheckIndependence:
    def check_independence(self, distr_table: pd.DataFrame):
        # write your solution here
        pass
```

Your function should also work with `distr_table`s other than the one given as an example. Apart from numpy and pandas packages, no other packages should be used.

## Expected Output Format

```python
{'are_independent': True/False, 'cov': <float>, 'corr': <float>}
```
"""
import numpy as np
import pandas as pd
import pytest
class CheckIndependence:
    def check_independence(self, distr_table):
        # P_X: Series with index = unique X values, values = P(X=x) (marginal)
        P_X = distr_table.groupby('X')['pr'].sum()
        # P_Y: Series with index = unique Y values, values = P(Y=y) (marginal)
        P_Y = distr_table.groupby('Y')['pr'].sum()

        # P_X.index holds the unique X values; P_X * P_X.index = Σ P(X=x)*x = E[X]
        mu_X = (P_X * P_X.index).sum()
        mu_Y = (P_Y * P_Y.index).sum()

        # Cov(X,Y) = Σᵢ pᵢ(xᵢ − μx)(yᵢ − μy), summed over all rows of the joint table
        cov = ((distr_table['X'] - mu_X) * (distr_table['Y'] - mu_Y) * distr_table['pr']).sum()

        # σx = sqrt( Σ P(X=x)(x − μx)² ), using the marginal distribution of X
        sigma_X = ((P_X * (P_X.index - mu_X) ** 2).sum()) ** 0.5
        sigma_Y = ((P_Y * (P_Y.index - mu_Y) ** 2).sum()) ** 0.5

        corr = cov / (sigma_X * sigma_Y) if sigma_X > 0 and sigma_Y > 0 else 0

        # Check P(X=x, Y=y) = P(X=x)*P(Y=y) for every row; use iterrows() to avoid
        # relying on a default RangeIndex
        are_independent = all(
            abs(row['pr'] - P_X[row['X']] * P_Y[row['Y']]) < 1e-9
            for _, row in distr_table.iterrows()
        )

        return {'are_independent': are_independent, 'cov': cov, 'corr': corr}
    
pytest_cases = [
    # cov=0.0525, corr=7/33≈0.2121 (verified by hand: E[XY]=0.75, E[X]=0.45, E[Y]=1.55)
    (pd.DataFrame({'X': [0, 0, 1, 1], 'Y': [1, 2, 1, 2], 'pr': [0.30, 0.25, 0.15, 0.30]}),
     {'are_independent': False, 'cov': 0.0525, 'corr': 7/33}),
    # equal joint probs → independent; pr must sum to 1.0 (was 0.225 each = 0.9 total)
    (pd.DataFrame({'X': [0, 0, 1, 1], 'Y': [1, 2, 1, 2], 'pr': [0.25, 0.25, 0.25, 0.25]}),
     {'are_independent': True, 'cov': 0.0, 'corr': 0.0}),
    # cov=-0.15, corr=-0.6 (symmetric marginals: P_X=P_Y=0.5, σx·σy=0.25)
    (pd.DataFrame({'X': [0, 0, 1, 1], 'Y': [1, 2, 1, 2], 'pr': [0.1, 0.4, 0.4, 0.1]}),
     {'are_independent': False, 'cov': -0.15, 'corr': -0.6}),
]
@pytest.mark.parametrize("distr_table, expected", pytest_cases)
def test_check_independence(distr_table, expected):
    checker = CheckIndependence()
    result = checker.check_independence(distr_table)
    assert result['are_independent'] == expected['are_independent']
    assert abs(result['cov'] - expected['cov']) < 1e-9
    assert abs(result['corr'] - expected['corr']) < 1e-9
