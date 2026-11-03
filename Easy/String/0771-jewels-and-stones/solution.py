"""
771. Jewels and Stones  (Easy)
https://leetcode.com/problems/jewels-and-stones/

Approach
--------
Each character in `stones` is a stone you own, and each character in
`jewels` is a type of stone that counts as a jewel. Walk through every
stone and add 1 to the count whenever that stone appears in `jewels`.

Note: `i in jewels` scans the jewels string, which is fine here because
the constraints keep both strings short (at most 50 characters). Using
set(jewels) would make each lookup O(1) on average.

Time:  O(n * m) - n = len(stones), m = len(jewels)
Space: O(1)     - just a counter
"""


class Solution(object):
    def numJewelsInStones(self, jewels, stones):

        count = 0
        for i in stones:
            if i in jewels:
                count += 1
        return count


# --- Solved example --------------------------------------------------------
# Input: jewels = "aA", stones = "aAAbbbb"
#
# 'a' in "aA" -> yes, count=1
# 'A' in "aA" -> yes, count=2
# 'A' in "aA" -> yes, count=3
# 'b' in "aA" -> no
# 'b' in "aA" -> no
# 'b' in "aA" -> no
# 'b' in "aA" -> no
#
# Output: 3

if __name__ == "__main__":
    s = Solution()
    print(s.numJewelsInStones("aA", "aAAbbbb"))   # 3
    print(s.numJewelsInStones("z", "ZZ"))         # 0
