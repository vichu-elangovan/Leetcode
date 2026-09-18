"""
9. Palindrome Number  (Easy)
https://leetcode.com/problems/palindrome-number/

Approach
--------
Convert the integer to a string and check whether it reads the same
forwards and backwards using slice reversal.

Note: this approach relies on string conversion. A follow-up variant of
this problem asks you to solve it without converting to a string
(compare digits by reversing the number mathematically instead).

Time:  O(n) - n = number of digits, for the conversion and reversal
Space: O(n) - for the string representation
"""


class Solution:
    def isPalindrome(self, x):
        s = str(x)
        return s == s[::-1]


# --- Solved example --------------------------------------------------------
# Input: x = 121
#
# s = "121"
# s[::-1] = "121"
# "121" == "121" -> True
#
# Output: True
#
# Input: x = -121
# s = "-121"
# s[::-1] = "121-"
# "-121" == "121-" -> False
#
# Output: False

if __name__ == "__main__":
    s = Solution()
    print(s.isPalindrome(121))    # True
    print(s.isPalindrome(-121))   # False
    print(s.isPalindrome(10))     # False
