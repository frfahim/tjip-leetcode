"""
TC: O(n*m)
MC: O(n)
Idea: find char freqency from every string and  store the frequency as a dict key
when two strings are anagram their frequency will be same, so they will be belongs to same dict keys

Test Cases:
["eat","tea","tan","ate","nat","bat"]
output = [["bat"],["nat","tan"],["ate","eat","tea"]]

["eat","tea","tana","ate","anat","bat", "aant"]
output = [["bat"],["aant","anat","tana"],["ate","eat","tea"]]
"""


class Solution:
    def groupAnagrams(self, strs: list[str]) -> list[list[str]]:
        """
        TC: O(m*nlog(n))
        MC: O(n)
        """
        # str_dict = {}
        # for string in strs:
        #     # sort every string before check and append to the dict
        #     sorted_str = "".join(sorted(string))
        #     if sorted_str not in str_dict:
        #         str_dict[sorted_str] = []
        #     str_dict[sorted_str].append(string)
        # return str_dict.values()

        """
        TC: O(m*n)
        MC: O(n)
        """
        str_dict = {}
        for string in strs:
            seen_char = [0]*26
            # find frequency of every char
            for char in string:
                seen_char[ord(char) - ord('a')] += 1
            # change to tuple, because tuple is immutable
            char_tuple = tuple(seen_char)
            # check the key and append to the dict
            if char_tuple not in str_dict:
                str_dict[char_tuple] = []
            str_dict[char_tuple].append(string)
        # return all values
        return str_dict.values()
