"""
2011. Final Value of Variable After Performing Operations  (Easy)
https://leetcode.com/problems/final-value-of-variable-after-performing-operations/

Approach
--------
Every operation is one of "++X", "X++", "--X", "X--". Whether the
operator is written before or after X doesn't change the final result,
so we only need to know if the operation is an increment or a decrement.
If the string contains '+', add 1 to x; otherwise it must be a '--'
operation, so subtract 1.

Time:  O(n) - single pass over the operations (each string has length 3)
Space: O(1) - just one counter
"""


class Solution(object):
    def finalValueAfterOperations(self, operations):
        x = 0
        for i in operations:
            if '+' in i:
                x += 1
            else:
                x -= 1
        return x


# --- Solved example --------------------------------------------------------
# Input: operations = ["--X", "X++", "X++"]
#
# x = 0
# "--X": no '+' in it -> x = 0 - 1 = -1
# "X++": has '+'      -> x = -1 + 1 = 0
# "X++": has '+'      -> x = 0 + 1 = 1
#
# Output: 1

if __name__ == "__main__":
    s = Solution()
    print(s.finalValueAfterOperations(["--X", "X++", "X++"]))         # 1
    print(s.finalValueAfterOperations(["++X", "++X", "X++"]))         # 3
    print(s.finalValueAfterOperations(["X++", "++X", "--X", "X--"]))  # 0
