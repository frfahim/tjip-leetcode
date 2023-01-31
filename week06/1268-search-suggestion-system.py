"""
Time Complexity: O(T + M * L)
O(T) for building Trie structure with all products, where T <= 2*10^4 is total number of characters in products.
O(M * L): In worst case, dfs to search up to 3 products can run up to O(L), where L is the length of the word which has largest length.
We need to dfs up to M times, where M <= 1000 is length of searchWord.

Space Complexity: O(T), it's total number of characters in the worst case when building Trie structure.
"""

from collections import defaultdict
from string import ascii_lowercase


# class TrieNode:
#     def __init__(self):
#         self.is_word = False
#         self.child = defaultdict(TrieNode)
#         self.word = None

#     def add_word(self, word):
#         current = self
#         for char in word:
#             current = current.child[char]
#         current.word = word
#         current.is_word = True

#     def get_suggested_words(self, prefix, limit=3):
#         words = []
#         head = self
#         def dfs(current):
#             if len(words) == limit:
#                 return
#             elif current.is_word:
#                 words.append(current.word)
#             for char in ascii_lowercase:
#                 if char in current.child:
#                     dfs(current.child[char])

#         for char in prefix:
#             if char not in head.child:
#                 return words
#             head = head.child[char]
#         dfs(head)
#         return words

#     def get_words(self, limit=3):
#         words = []
#         def dfs(current):
#             if len(words) == limit:
#                 return
#             elif current.is_word:
#                 words.append(current.word)
#             for char in ascii_lowercase:
#                 if char in current.child:
#                     dfs(current.child[char])

#         dfs(self)
#         return words

# class Solution:
#     def suggestedProducts(self, products: list[str], searchWord: str) -> list[list[str]]:
#         trie = TrieNode()
#         results = []
#         for product in products:
#             trie.add_word(product)

#         # prefix = ""
#         # for char in searchWord:
#         #     prefix += char
#         #     results.append(trie.get_suggested_words(prefix))

#         current = trie
#         for char in searchWord:
#             if current and char in current.child:
#                 current = current.child[char]
#                 results.append(current.get_words(limit=3))
#             else:
#                 current = None
#                 results.append([])
#         return results


"""
Sort
n = number of charcters in the products list
Time: O(nlog(n))

Build Trie
k = 3
m = number of characters in the longest product
Time: O(n)
Space: O(nkm)

Output Result
s = number of characters in searchword
Time: O(s)
Space: O(sk)
"""


class Trie:
    def __init__(self, suggestion_limit = 3):
        self.child = defaultdict(Trie)
        self.suggested_words = []
        self.suggestion_limit = suggestion_limit

    def add_word(self, word):
        current = self
        for char in word:
            current = current.child[char]
            self.add_suggetion(current, word)

    def add_suggetion(self, node, word):
        if len(node.suggested_words) < self.suggestion_limit:
            node.suggested_words.append(word)

    def get_suggestion(self, search_word):
        results = []
        current = self
        for char in search_word:
            current = current.child[char]
            results.append(current.suggested_words)
        return results

class Solution:
    def suggestedProducts(self, products: list[str], search_word: str) -> list[list[str]]:
        trie = Trie()
        results = []
        products.sort()
        for product in products:
            trie.add_word(product)

        results = trie.get_suggestion(search_word)
        return results
