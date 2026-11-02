"""
1672. Richest Customer Wealth  (Easy)
https://leetcode.com/problems/richest-customer-wealth/

Approach
--------
Each row of `accounts` is one customer and each value in the row is the
money in one of their bank accounts. A customer's wealth is the sum of
their row. Compute the sum for every row with a generator expression and
return the maximum, without building an intermediate list.

Time:  O(m * n) - m customers, n accounts each, every value is summed once
Space: O(1)     - the generator yields one sum at a time
"""


class Solution(object):
    def maximumWealth(self, accounts):

        return max(sum(customer) for customer in accounts)


# --- Solved example --------------------------------------------------------
# Input: accounts = [[1, 2, 3], [3, 2, 1]]
#
# customer [1, 2, 3] -> 1 + 2 + 3 = 6
# customer [3, 2, 1] -> 3 + 2 + 1 = 6
#
# max(6, 6) = 6
#
# Output: 6
#
# Input: accounts = [[1, 5], [7, 3], [3, 5]]
#
# customer [1, 5] -> 6
# customer [7, 3] -> 10
# customer [3, 5] -> 8
#
# max(6, 10, 8) = 10
#
# Output: 10

if __name__ == "__main__":
    s = Solution()
    print(s.maximumWealth([[1, 2, 3], [3, 2, 1]]))          # 6
    print(s.maximumWealth([[1, 5], [7, 3], [3, 5]]))        # 10
    print(s.maximumWealth([[2, 8, 7], [7, 1, 3], [1, 9, 5]]))  # 17
