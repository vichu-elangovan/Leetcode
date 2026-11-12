"""
67. Add Binary  (Easy)
https://leetcode.com/problems/add-binary/

Approach
--------
Add the two binary strings the way you would on paper: start from the
rightmost digits and move left, carrying as you go.
- Use two pointers, i and j, starting at the last index of a and b.
- At each step, total = carry + a[i] (if any left) + b[j] (if any left).
- The digit to write down is total % 2, and the new carry is total // 2.
- Keep going while either string has digits left OR a carry remains
  (this handles the final extra digit, e.g. "1" + "1" = "10").
- Digits are collected from right to left, so reverse them at the end.

Time:  O(max(n, m)) - one pass over the longer string
Space: O(max(n, m)) - the result list
"""


class Solution(object):
    def addBinary(self, a, b):
        res = []
        carry = 0
        i, j = len(a) - 1, len(b) - 1

        while i >= 0 or j >= 0 or carry:
            total = carry

            if i >= 0:
                total += int(a[i])
                i -= 1
            if j >= 0:
                total += int(b[j])
                j -= 1

            res.append(str(total % 2))
            carry = total // 2

        return "".join(reversed(res))


# --- Solved example --------------------------------------------------------
# Input: a = "11", b = "1"
#
# i=1, j=0, carry=0
#
# step1: total = 0 + a[1]=1 + b[0]=1 = 2 -> write 0, carry=1   res=['0']
# step2: total = 1 + a[0]=1          = 2 -> write 0, carry=1   res=['0','0']
# step3: i<0, j<0 but carry=1: total = 1 -> write 1, carry=0   res=['0','0','1']
#
# reverse res -> "100"
#
# Output: "100"

if __name__ == "__main__":
    s = Solution()
    print(s.addBinary("11", "1"))        # 100
    print(s.addBinary("1010", "1011"))   # 10101
    print(s.addBinary("0", "0"))         # 0
