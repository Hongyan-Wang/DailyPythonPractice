"""
https://leetcode.com/discuss/post/4991818/microssoft-oa-by-anonymous_user-i0x0/

A technology company announced that a new supply of P monitors would soon be available at their store, There
were N orders (numbered from 0 to N-1) placed by customers who wanted to buy those monitors. The K-th order
has to be delivered to a location at distance DIK] from the store and is for exactly CK] monitors.

Now the time has come for the monitors to be delivered. The orders will be fulfilled one by one. To minimize the
shipping time, it has been decided that the deliveries will be made in order of increasing distance from the store.
If there are many customers at the same distance, they can be processed in any order. Monitors to more distant
customers will be delivered only once all orders to customers closer to the store have already been fulfilled.

What is the maximum total number of orders that can be fulfilled?
Write a function:

class solution { public iat solution(int(] D, imt(] C, int P); }

that, given two arrays of integers D and C, and an integer P. returns the maximum total number of orders that can
be fulfilled.

Examples:

1. GivenD =[5,11,1,3], C=[6, 1,3, 2] and P = 7, the function should return 2. The customers at distances 1 and
3 will have their orders fulfilled and 3 + 2 = 5 monitors will be delivered. 

2. Given D =[10, 15,1], C =[10, 1, 2] and P = 3, the function should return 1. Only the order for the customer at
distance 1 will be fulfilled. There will not be enough monitors in the store for the customer at distance 10. 
Therefore, orders for customers at distances 10 and 15 will not be fulfilled.

3. GivenD=[11,18,1],C=[9, 18, 8] and P = 7, the function should return 0. 

4. GivenD=[1,4,2,5],C=[4,9,2, 3] and P = 19, the function should return 4. 

Write an efficient algorithm for the following assumptions:
N is an integer within the [1..100,000};
Each element of arrays D and C is an integer within the range [1..1,000,000,000];
P is an integer within the range [0...1000000000]


"""

import pytest

def solution(D, C, P):
    orders = sorted(zip(D, C), key=lambda x: (x[0], x[1]))
    for i, (d, c) in enumerate(orders):
        if P < c:
            return i
        P -= c
    return len(orders)
"""
Notes:

This problem mainly tests the ability to sort and iterate through the orders while keeping track of the remaining monitors (P). The key steps are:
1. Zip the distance and count arrays together to create a list of orders.
2. Sort the orders based on distance.
3. Iterate through the sorted orders, fulfilling them until we run out of monitors (P).

**Corner Cases**:
- If P is less than the count of any single order, that order cannot be fulfilled.
- If P is greater than or equal to the sum of all counts, all orders can be fulfilled.
- If there are multiple orders at the same distance, they can be processed in any order, 
    but since we are sorting by distance, they will be processed in the order they appear in the input.
    In this case, we should also sort by count to ensure that we fulfill smaller orders first when distances are the same, which can help maximize the number of fulfilled orders.


**Time Complexity**: 
The sorting step takes O(N log N), and the iteration step takes O(N). Therefore, the overall time complexity is O(N log N).
**Space Complexity**: 
We create a new list of zipped orders which takes O(N) space. The sorting is done in-place, so it does not require additional space. Therefore, the overall space complexity is O(N).

"""


@pytest.mark.parametrize("D, C, P, expected", [
    ([5, 11, 1, 3], [6, 1, 3, 2], 7, 2),
    ([10, 15, 1], [10, 1, 2], 3, 1),
    ([11, 18, 1], [9, 18, 8], 7, 0),
    ([1, 4, 2, 5], [4, 9, 2, 3], 19, 4),
    ([1, 1, 2], [8, 1, 1], 2, 1),
    ([1, 1, 1], [2, 1, 3], 3, 2),
    ([5, 2, 8], [3, 1, 4], 8, 3),
    ([1, 2, 3], [1, 1, 1], 0, 0),
    ([1, 2, 3], [5, 1, 1], 4, 0),
    ([10], [5], 5, 1),
    ([10], [5], 4, 0),
])
def test_solution(D, C, P, expected):
    assert solution(D, C, P) == expected    
