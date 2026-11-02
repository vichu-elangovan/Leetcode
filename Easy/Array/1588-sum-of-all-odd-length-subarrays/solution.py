"""
1588. Sum of All Odd Length Subarrays  (Easy)
https://leetcode.com/problems/sum-of-all-odd-length-subarrays/

Approach
--------
Instead of generating every odd-length subarray, count how many of them
each element appears in and add up its contribution.

For the element at index i:
- (i + 1) choices for where a subarray starts (at or before i)
- (n - i) choices for where it ends (at or after i)
- so it appears in (i + 1) * (n - i) subarrays in total

Roughly half of those subarrays have odd length. Precisely, the number
of odd-length ones is (total_subarrays + 1) // 2, so the element adds
odd_occurrences * arr[i] to the answer.

Time:  O(n) - single pass
Space: O(1) - just a running total
"""


class Solution(object):
    def sumOddLengthSubarrays(self, arr):
        total_sum = 0
        n = len(arr)

        for i in range(n):
            total_subarrays = (i + 1) * (n - i)

            odd_occurrences = (total_subarrays + 1) // 2

            total_sum += odd_occurrences * arr[i]

        return total_sum


# --- Solved example --------------------------------------------------------
# Input: arr = [1, 4, 2, 5, 3]   (n = 5)
#
# i=0 (1): total = 1*5 = 5,  odd = (5+1)//2 = 3  -> adds 3*1 = 3
# i=1 (4): total = 2*4 = 8,  odd = (8+1)//2 = 4  -> adds 4*4 = 16
# i=2 (2): total = 3*3 = 9,  odd = (9+1)//2 = 5  -> adds 5*2 = 10
# i=3 (5): total = 4*2 = 8,  odd = (8+1)//2 = 4  -> adds 4*5 = 20
# i=4 (3): total = 5*1 = 5,  odd = (5+1)//2 = 3  -> adds 3*3 = 9
#
# total_sum = 3 + 16 + 10 + 20 + 9 = 58
#
# Output: 58

if __name__ == "__main__":
    s = Solution()
    print(s.sumOddLengthSubarrays([1, 4, 2, 5, 3]))   # 58
    print(s.sumOddLengthSubarrays([1, 2]))            # 3
    print(s.sumOddLengthSubarrays([10, 11, 12]))      # 66
