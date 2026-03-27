"""
Check if random variables are independent You are given a table distr_table with a joint probability
distribution of two random variables X and Y, for example
| X | Y | P(X, Y) |
|-----|-----|-----------|
| 0   | 1   | 0.30      |
| 0   | 2   | 0.25      |
| 1   | 1   | 0.15      |
| 1   | 2   | 0.30      |

As you can see, for example P(X = 0 & Y = 1) = 0.3, P(Y = 1) = 0.3 + 0.15 = 0.45
Probabilities in a third column add up to 1. 
Write a method check_independence O that for a given
distr_table D returns a dictionary of length 3, where
• first element (the kev named are_indenendent is a boolean value which states if X and Y are independent (True) or not (False);
• second element (the key named cov) is a covariance between X and Y (i is an indicator of i-th of n possible pairs (x_i, y_i) of (X, Y));
• third element (the key named corr) is a correlation between X and Y.

You should implement your function to work also with different
distr_table D s than a given as an example. 
"""
