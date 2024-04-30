# Given a string containing digits from 2-9 inclusive, return all possible letter combinations that the number could represent. Return the answer in any order.
# A mapping of digits to letters (just like on the telephone buttons) is given below. Note that 1 does not map to any letters.
from typing import List

# Example 1:
# Input: digits = "23"
# Output: ["ad","ae","af","bd","be","bf","cd","ce","cf"]
input = "23"
expected = ["ad", "ae", "af", "bd", "be", "bf", "cd", "ce", "cf"]


# # Example 2:
# # Input: digits = ""
# # Output: []
# input = ""
# expected = []

# # Example 3:
# # Input: digits = "2"
# # Output: ["a","b","c"]
# input = "2"
# expected = ["a", "b", "c"]

class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        def dfs(index, path):
            # 끝까지 탐색하면 백트래킹
            if len(path) == len(digits):
                result.append(path)
                return

            # 입력값 자릿수 단위 반복
            for i in range(index, len(digits)):
                # 숫자에 해당하는 모든 문자열 반복
                for c in dic[digits[i]]:
                    dfs(i + 1, path + c)

        # 예외 처리
        if not digits:
            return []

        result = []
        dic = {
            '2': 'abc', '3': 'def', '4': 'ghi', '5': 'jkl',
            '6': 'mno', '7': 'pqrs', '8': 'tuv', '9': 'wxyz'}

        dfs(0, '')
        return result


s = Solution()
result = s.letterCombinations(input)
print(expected == result, result)
