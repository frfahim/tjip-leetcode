class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        # if len(s) != len(t):
        #     return False
        # str1 = sorted(s)
        # str2 = sorted(t)
        # for ind, chr in enumerate(str1):
        #     if chr != str2[ind]:
        #         return False
        # return True

        if len(s) != len(t):
            return False
        seen_char = [0]*26
        for ind, chr in enumerate(s):
            seen_char[ord(chr) - ord('a')] += 1
            seen_char[ord(t[ind]) - ord('a')] -= 1

        for val in seen_char:
            if val != 0:
                return False
        return True
