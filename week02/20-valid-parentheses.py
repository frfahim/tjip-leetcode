"""
TC: O(n)
MC: O(n)
Idea: append visited open symbols in stack. when closing symbol found
check last value from stack and if they are not in pair return False or return True

Test Cases:
"()" = True
"()[]{}" = True
"(]" = False
"({[]}{})" = True
"""

class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        symbols = {'(': ')', '{': '}', '[': ']'}
        for sym in s:
            if sym in symbols:
                stack.append(sym)
            elif not stack or symbols[stack.pop()] != sym:
                return False
        return False if stack else True
