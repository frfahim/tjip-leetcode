"""
TC:
MC:

Idea:
Implement Trie with words from wordDict.
Add a list to track a word is exist and update index with True and False.
Solved using Trie and DP.
explanation: https://www.youtube.com/watch?v=iWenZCZEBIA

Test Cases:

"leetcode"
["leet","code"]
"leetcode"
["leet","ode"]
"leetcode"
["eet", "lee", "code"]
"leetcode"
["le", "et","co", "de"]
"leetcode"
["leet","cod", "de"]
"catsandog"
["cats","dog","sand","and","cat"]
"catsandog"
["cats","dog","sand","an","cat"]
"aaaaaaaaaaaaaaaaaaaaaaaaab"
["a","aa","aaa","aaaa","aaaaa"]
"""


# Trie Implementation

class Trie:
    def __init__(self):
        self.is_end = False
        self.children = {}


class Solution:
    def __init__(self):
        self.root = Trie()

    def insert(self, word):
        current = self.root
        for char in word:
            if char not in current.children:
                current.children[char] = Trie()
            current = current.children[char]
        current.is_end = True

    # this trie search also work
    # def search(self, string, start, visited_index=set()):
    #     current = self.root
    #     if start >= len(string):
    #         return True
    #     for ind in range(start, len(string)):
    #         if string[ind] not in current.children:
    #             return False
    #         current = current.children[string[ind]]
    #         if current.is_end and ind+1 not in visited_index:
    #             visited_index.add(ind+1)
    #             if self.search(string, ind+1, visited_index):
    #                 return True
    #         ind += 1
    #     return False

    # this trie search also work
    def search(self, word) -> bool:
        current = self.root
        for char in word:
            if char not in current.children:
                return False
            current = current.children[char]
        return current.is_end

    def match_words(self, string):
        dp = [False] * (len(string) + 1)
        dp[0] = True

        for ind in range(1, len(string) + 1):
            for ind2 in range(ind):
                if dp[ind2] and self.search(string[ind2:ind]):
                    dp[ind] = True
                    break
        return dp[-1]

    def wordBreak(self, s: str, wordDict: List[str]) -> bool:
        for word in wordDict:
            self.insert(word)

        return self.match_words(s)