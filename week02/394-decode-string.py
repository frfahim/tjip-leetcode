"""
TC: O(n)
MC: O(n)
Idea:

Test Cases:
"3[a]2[bc]"
"5[2[a]]"
"2[abc]3[cd]ef"
"2[abc2[z]]3[cd]ef"
"3[2[abc5[z]]4[de]tr]"
"""

class Solution:
    def decodeString(self, s: str) -> str:
        # stack = []
        # digit_times = 0
        # latest_str = ""
        # for char in s:
        #     if char.isdigit():
        #         digit_times = (digit_times * 10) + int(char)
        #     elif char == "[":
        #         stack.append((latest_str, digit_times))
        #         latest_str = ""
        #         digit_times = 0
        #     elif char == ']':
        #         last_item = stack.pop()
        #         latest_str = last_item[0] + (latest_str * last_item[1])
        #     else:
        #         latest_str += char

        # return latest_str

        stack = [("", 1)]
        digit_times = 0
        for ind, char in enumerate(s):
            if char.isdigit():
                digit_times = (digit_times * 10) + int(char)
            elif char == '[':
                stack.append(("", digit_times))
                digit_times = 0
            elif char == ']':
                last = stack.pop()
                new_str = last[1] * last[0]
                last = stack.pop()
                stack.append((last[0] + new_str, last[1]))
            else:
                last = stack.pop()
                stack.append((last[0] + char, last[1]))
        return stack.pop()[0]
