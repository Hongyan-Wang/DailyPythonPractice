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
