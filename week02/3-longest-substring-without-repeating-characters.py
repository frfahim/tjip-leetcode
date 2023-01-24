"""
TC: O(n)
MC: O(n)
Idea:

Test Cases:
"abcabcbb" = 3
"bbbbb" = 1
"pwwkew" = 3
"abbxyzzcr" = 4
"""

class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        left_point, right_point, duplicate_count, max_len = 0, 0, 0, 0
        repeated_allowed = 1
        seen_char = {}

        while right_point < len(s):
            # add a char to the map
            if seen_char.get(s[right_point]):
                seen_char[s[right_point]] += 1
            else:
                seen_char[s[right_point]] = 1

            # check the char is duplicated, for this its allowing only 1 repeating
            if seen_char[s[right_point]] > repeated_allowed:
                duplicate_count += 1

            # check duplicate, if duplicate then move left pointer 1 step and if left and righ point same
            # then decrease duplicate count by 1
            while (duplicate_count > 0):
                seen_char[s[left_point]] -= 1
                if seen_char[s[left_point]] == seen_char[s[right_point]]:
                    duplicate_count -= 1
                left_point += 1

            # calculate current max lenght
            max_len = max(max_len, (right_point - left_point + 1))
            # move right pointer 1 step ahead
            right_point += 1
        return max_len
