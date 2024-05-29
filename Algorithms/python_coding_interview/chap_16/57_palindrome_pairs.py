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

class Solution:
    def palindromePairs(self, words: List[str]) -> List[List[int]]:
        #1. 팰린드롬을 브루트 포스로 계산
        def is_palindrome(word):
            return word == word[::-1]

        output = []
        for i, word1 in enumerate(words):
            for j, word2 in enumerate(words):
                if i == j:
                    continue
                if is_palindrome(word1 + word2):
                    output.append([i, j])
        return output


s = Solution()
result = s.palindromePairs(input)
print(expected == result, result)
