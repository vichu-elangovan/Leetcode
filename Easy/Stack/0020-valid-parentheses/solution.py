"""
20. Valid Parentheses  (Easy)
https://leetcode.com/problems/valid-parentheses/

Approach
--------
Use a stack. Every time we see an opening bracket, push the *matching
closing* bracket onto the stack (a neat trick — it means we don't need
a separate lookup when we hit a closer, just compare directly). Every
time we see a closing bracket, it must equal whatever is on top of the
stack; if the stack is empty or it doesn't match, the string is invalid.
At the end, the stack must be empty (every open was closed).

Time:  O(n) - single pass over the string
Space: O(n) - worst case, all characters are opening brackets
"""


class Solution:
    def isValid(self, s):
        stack = []

        for ch in s:

            if ch == '(':
                stack.append(')')

            elif ch == '{':
                stack.append('}')

            elif ch == '[':
                stack.append(']')

            else:
                if not stack or stack.pop() != ch:
                    return False

        return len(stack) == 0


# --- Solved example --------------------------------------------------------
# Input: s = "{[()]}"
#
# ch='{'  push '}'   -> stack = ['}']
# ch='['  push ']'   -> stack = ['}', ']']
# ch='('  push ')'   -> stack = ['}', ']', ')']
# ch=')'  pop -> ')' matches ch  -> stack = ['}', ']']
# ch=']'  pop -> ']' matches ch  -> stack = ['}']
# ch='}'  pop -> '}' matches ch  -> stack = []
#
# stack is empty -> return True
#
# Output: True

if __name__ == "__main__":
    s = Solution()
    print(s.isValid("()"))       # True
    print(s.isValid("()[]{}"))   # True
    print(s.isValid("(]"))       # False
    print(s.isValid("{[()]}"))   # True
