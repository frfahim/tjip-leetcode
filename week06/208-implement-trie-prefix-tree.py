"""
Trie Insert:
TC : O(m) where m is the key length.
MC: O(m)
Trie Search:
TC : O(m) where m is the key length.
MC: O(1)
Trie Prefix Search:
TC : O(m) where m is the key length.
MC: O(1)

"""

# class TrieNode:
#     def __init__(self):
#         char_limit = 26
#         self.is_end = False
#         self.next = [None] * char_limit


# class Trie:

#     def __init__(self):
#         self.root = TrieNode()

#     def insert(self, word: str) -> None:
#         current = self.root
#         for char in word:
#             ind = ord(char) - ord('a')
#             if current.next[ind] == None:
#                 current.next[ind] = TrieNode()
#             current = current.next[ind]
#         current.is_end = True
        

#     def search(self, word: str, is_prefix: bool = False) -> bool:
#         current = self.root
#         for char in word:
#             ind = ord(char) - ord('a')
#             if current.next[ind] == None:
#                 return False
#             current = current.next[ind]
#         return True if is_prefix else current.is_end
        

#     def startsWith(self, prefix: str) -> bool:
#         return self.search(prefix, is_prefix=True)
        


class TrieNode:
    def __init__(self):
        self.is_end = False
        self.children = {}


class Trie:

    def __init__(self):
        self.root = TrieNode()

    def insert(self, word: str) -> None:
        current = self.root
        for char in word:
            if char not in current.children:
                current.children[char] = TrieNode()
            current = current.children[char]
        current.is_end = True

    def search(self, word: str, is_prefix: bool = False) -> bool:
        current = self.root
        for char in word:
            if char not in current.children:
                return False
            current = current.children[char]
        return True if is_prefix else current.is_end

    def startsWith(self, prefix: str) -> bool:
        return self.search(prefix, is_prefix=True)
