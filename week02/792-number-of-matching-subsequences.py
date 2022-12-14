"""
TC: O(N*W*log(S))
MC: O(n)

Idea: Store indices of S in list of dict. Iterate in every char from words,
binary search on the indices list from S, check char is exist and
index is less than current char index. If true return 1 or 0

Test Cases:
"abcde"
["a","bb","acd","ace"]
output = 3
"dsahjpjauf",
["ahjpjau","ja","ahbwzgqnuk","tnmlanowax"]
output = 2
"baxxxxxxxbbyyyyyc"
["abc", "xy", "xyc", "abyc", "xyz", "yxc", "yc", "xyc", "xyb", "xby"]
output = 7
"""

import bisect
from collections import defaultdict

class Solution:
    def numMatchingSubseq(self, s: str, words: list[str]) -> int:
        # decalring as defaultdict so that if any char from words doesn't belogs in S
        # then it will return empty list, that is useful for bisect_left
        char_indexes = defaultdict(list)
        matching_count = 0

        def is_subseq(word):
            cur_ind = -1
            for char in word:
                # from the list of current char indices, find index which is larger from cur_ind 
                ind = bisect.bisect_left(char_indexes[char], cur_ind + 1)
                # return False if ind is equual to the len of char indices list
                # means this char is not in sub sequences
                if ind == len(char_indexes[char]):
                    return False
                cur_ind = char_indexes[char][ind]
            return True

        # append indexes of every char in a list of dict
        for ind, char in enumerate(s):
            char_indexes[char].append(ind)
        for word in words:
            matching_count += is_subseq(word)
        return matching_count
