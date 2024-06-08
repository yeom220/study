# You are given a 0-indexed array of unique strings words.
#
# A palindrome pair is a pair of integers (i, j) such that:
#
# 0 <= i, j < words.length,
# i != j, and
# words[i] + words[j] (the concatenation of the two strings) is a
# palindrome
# .
# Return an array of all the palindrome pairs of words.
#
# You must write an algorithm with O(sum of words[i].length) runtime complexity.
import collections
from typing import List

# Example 1:
# Input: words = ["abcd","dcba","lls","s","sssll"]
# Output: [[0,1],[1,0],[3,2],[2,4]]
# Explanation: The palindromes are ["abcddcba","dcbaabcd","slls","llssssll"]
input = ["abcd", "dcba", "lls", "s", "sssll"]
expected = [[0, 1], [1, 0], [3, 2], [2, 4]]


# # Example 2:
# # Input: words = ["bat","tab","cat"]
# # Output: [[0,1],[1,0]]
# # Explanation: The palindromes are ["battab","tabbat"]
# input = ["bat", "tab", "cat"]
# expected = [[0, 1], [1, 0]]

# # Example 3:
# # Input: words = ["a",""]
# # Output: [[0,1],[1,0]]
# # Explanation: The palindromes are ["a","a"]
# input = ["a", ""]
# expected = [[0, 1], [1, 0]]

# 트라이를 저장할 노드
class TrieNode:
    def __init__(self):
        self.children = collections.defaultdict(TrieNode)
        self.word_id = -1
        self.palindrome_word_ids = []


class Trie:
    def __init__(self):
        self.root = TrieNode()

    @staticmethod
    def is_palindrome(word: str) -> bool:
        return word[::] == word[::-1]

    # 단어 삽입
    def insert(self, index, word) -> None:
        node = self.root
        for i, char in enumerate(reversed(word)):
            if self.is_palindrome(word[0:len(word) - i]):
                node.palindrome_word_ids.append(index)
            node = node.children[char]
            node.val = char
        node.word_id = index

    def search(self, index, word) -> List[List[int]]:
        result = []
        node = self.root

        while word:
            # 판별 로직
            if node.word_id >= 0:
                if self.is_palindrome(word):
                    result.append([index, node.word_id])
            if not word[0] in node.children:
                return result
            node = node.children[word[0]]
            word = word[1:]

        # 판별 로직
        if node.word_id >= 0 and node.word_id != index:
            result.append([index, node.word_id])

        # 판별 로직
        for palindrome_word_id in node.palindrome_word_ids:
            result.append([index, palindrome_word_id])

        return result


class Solution:
    def palindromePairs(self, words: List[str]) -> List[List[int]]:
        # # 1. 팰린드롬을 브루트 포스로 계산
        # def is_palindrome(word):
        #     return word == word[::-1]
        #
        # output = []
        # for i, word1 in enumerate(words):
        #     for j, word2 in enumerate(words):
        #         if i == j:
        #             continue
        #         if is_palindrome(word1 + word2):
        #             output.append([i, j])
        # return output

        # 트라이 구현
        trie = Trie()

        for i, word in enumerate(words):
            trie.insert(i, word)

        results = []
        for i, word in enumerate(words):
            results.extend(trie.search(i, word))

        return results


s = Solution()
result = s.palindromePairs(input)
print(expected == result, result)
