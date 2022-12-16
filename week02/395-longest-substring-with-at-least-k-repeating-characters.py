"""
TC: O(N) # O(|s|*n)
MC: O(N)

Test Cases:
"aaabb"
3
output = 3
"ababbc"
2
output = 5
"abacb"
2
output = 0
"abbacb"
2
output = 4
"abaccb"
2
output = 6
"aaaabbcddaeaaff"
2
output = 6
"aaaabbcddaeaaff"
3
output = 4
"""

from collections import defaultdict
class Solution:
    def get_long_subs_with_unique_char(self, string, min_freq, max_unique_char):
        left_point, right_point, max_len = 0, 0, 0
        # using defaultdict, so that we don't need to handle dict key error of no exist key value increment
        seen_char = defaultdict(int)
        unique_char_cnt = 0 # count how many unique char
        freq_char_cnt = 0 # calculate how many char count has at least min_freq
        while right_point < len(string):
            seen_char[string[right_point]] += 1
            unique_char_cnt += (seen_char[string[right_point]] == 1)
            freq_char_cnt += (seen_char[string[right_point]] == min_freq)
            right_point += 1

            while unique_char_cnt > max_unique_char:
                seen_char[string[left_point]] -= 1
                unique_char_cnt -= (seen_char[string[left_point]] == 0)
                freq_char_cnt -= (seen_char[string[left_point]] == min_freq - 1)
                left_point += 1

            if unique_char_cnt == freq_char_cnt:
                max_len = max(max_len, right_point - left_point)
        return max_len

    def longestSubstring(self, s: str, k: int) -> int:

        max_len = 0
        for unique_char_cnt in range(0, 26):
            max_len = max(max_len, self.get_long_subs_with_unique_char(s, k, unique_char_cnt))
        return max_len
