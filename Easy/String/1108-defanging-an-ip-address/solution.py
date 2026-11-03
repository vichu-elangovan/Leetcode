"""
1108. Defanging an IP Address  (Easy)
https://leetcode.com/problems/defanging-an-ip-address/

Approach
--------
A defanged IP address replaces every "." with "[.]". Python's built-in
str.replace() does exactly that in one call, swapping every occurrence
of '.' for '[.]' and returning the new string.

Time:  O(n) - replace scans the string once
Space: O(n) - the new string is slightly longer than the original
"""


class Solution(object):
    def defangIPaddr(self, address):
        return address.replace('.', '[.]')


# --- Solved example --------------------------------------------------------
# Input: address = "1.1.1.1"
#
# replace '.' with '[.]' at each of the three dots:
#   "1.1.1.1" -> "1[.]1.1.1" -> "1[.]1[.]1.1" -> "1[.]1[.]1[.]1"
#
# Output: "1[.]1[.]1[.]1"
#
# Input: address = "255.100.50.0"
#
# Output: "255[.]100[.]50[.]0"

if __name__ == "__main__":
    s = Solution()
    print(s.defangIPaddr("1.1.1.1"))         # 1[.]1[.]1[.]1
    print(s.defangIPaddr("255.100.50.0"))    # 255[.]100[.]50[.]0
