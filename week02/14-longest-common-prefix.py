"""
TC: O(n)
MC: O(1)

Idea: compare every char from first string with rest of the string.
if there any mismitch then return string till first string.

Test cases:
["flower","flow","flight"] = "fl"
["flower","glow","flight"] = ""
["flower","flow","flight"]
"""

class Solution:
    def longestCommonPrefix(self, strs: list[str]) -> str:

        # Approach 1:
        # find minimun string and compare this string char with other
        # from which position char are mismitch till that is our expected result.

        # min_str = min(strs)
        # max_str = max(strs)
        # # result = ""
        # for ind, char in enumerate(min_str):
        #     if char != max_str[ind]:
        #         # return result
        #         return min_str[:ind]
        #     # result += char
        # return min_str

        # Approach 2:
        # checking_str = strs[0]
        # result = ""
        # for ind, char in enumerate(str[0]):
        #     for string in strs:
        #         if ind == len(string) or char != string[ind]:
        #             return result
        #     result += char
        # return result

        for ind, char in enumerate(strs[0]):
            for string in strs:
                if ind == len(string) or char != string[ind]:
                    return strs[0][:ind]
        return strs[0]
