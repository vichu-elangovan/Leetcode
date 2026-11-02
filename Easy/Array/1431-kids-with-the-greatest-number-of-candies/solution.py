"""
1431. Kids With the Greatest Number of Candies  (Easy)
https://leetcode.com/problems/kids-with-the-greatest-number-of-candies/

Approach 1: Brute force
-----------------------
For each kid, add extraCandies to their count, then compare that total
against every kid's candies. If the total is smaller than anyone's count,
this kid can't have the greatest number, so mark False and stop early.

Time:  O(n^2) - for each kid, scan all kids
Space: O(n)   - the output list

Approach 2: Find the max once (optimal)
---------------------------------------
A kid ends up with the greatest number exactly when their candies plus
extraCandies is at least the current maximum. Compute the maximum once,
then check each kid against it in a single pass.

Time:  O(n) - one pass to find the max, one pass to build the result
Space: O(n) - the output list
"""


class Solution(object):
    def kidsWithCandies(self, candies, extraCandies):

        res = []

        for i in range(len(candies)):
            total = candies[i] + extraCandies
            is_greatest = True

            for j in range(len(candies)):
                if total < candies[j]:
                    is_greatest = False
                    break

            res.append(is_greatest)

        return res


class SolutionOptimized(object):
    def kidsWithCandies(self, candies, extraCandies):
        max_candies = max(candies)
        return [candy + extraCandies >= max_candies for candy in candies]


# --- Solved example --------------------------------------------------------
# Input: candies = [2, 3, 5, 1, 3], extraCandies = 3
#
# max_candies = 5
#
# kid 0: 2 + 3 = 5 >= 5  -> True
# kid 1: 3 + 3 = 6 >= 5  -> True
# kid 2: 5 + 3 = 8 >= 5  -> True
# kid 3: 1 + 3 = 4 <  5  -> False
# kid 4: 3 + 3 = 6 >= 5  -> True
#
# Output: [True, True, True, False, True]

if __name__ == "__main__":
    for sol in (Solution(), SolutionOptimized()):
        print(sol.kidsWithCandies([2, 3, 5, 1, 3], 3))   # [True, True, True, False, True]
        print(sol.kidsWithCandies([4, 2, 1, 1, 2], 1))   # [True, False, False, False, False]
        print(sol.kidsWithCandies([12, 1, 12], 10))      # [True, False, True]
