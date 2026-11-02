"""
1470. Shuffle the Array  (Easy)
https://leetcode.com/problems/shuffle-the-array/

Approach
--------
nums has 2n elements: the first half is x1..xn and the second half is
y1..yn. The answer interleaves them as x1, y1, x2, y2, ... For each
index i in the first half, append nums[i] and then its partner from the
second half, nums[i + n].

Time:  O(n) - single pass over n pairs
Space: O(n) - the output array of size 2n
"""


class Solution(object):
    def shuffle(self, nums, n):
        res = []
        for i in range(n):
            res.append(nums[i])
            res.append(nums[i + n])
        return res


# --- Solved example --------------------------------------------------------
# Input: nums = [2, 5, 1, 3, 4, 7], n = 3
#
# first half = [2, 5, 1], second half = [3, 4, 7]
#
# i=0: append nums[0]=2, nums[3]=3  -> res = [2, 3]
# i=1: append nums[1]=5, nums[4]=4  -> res = [2, 3, 5, 4]
# i=2: append nums[2]=1, nums[5]=7  -> res = [2, 3, 5, 4, 1, 7]
#
# Output: [2, 3, 5, 4, 1, 7]

if __name__ == "__main__":
    s = Solution()
    print(s.shuffle([2, 5, 1, 3, 4, 7], 3))        # [2, 3, 5, 4, 1, 7]
    print(s.shuffle([1, 2, 3, 4, 4, 3, 2, 1], 4))  # [1, 4, 2, 3, 3, 2, 4, 1]
    print(s.shuffle([1, 1, 2, 2], 2))              # [1, 2, 1, 2]
