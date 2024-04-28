# Given a string s, find the length of the longest substring without repeating characters.

# Example 1:
# Input: s = "abcabcbb"
# Output: 3
# Explanation: The answer is "abc", with the length of 3.
input = "abcabcbb"
expected = 3


# # Example 2:
# # Input: s = "bbbbb"
# # Output: 1
# # Explanation: The answer is "b", with the length of 1.
# input = "bbbbb"
# expected = 1

# # Example 3:
# # Input: s = "pwwkew"
# # Output: 3
# # Explanation: The answer is "wke", with the length of 3.
# # Notice that the answer must be a substring, "pwke" is a subsequence and not a substring.
# input = "pwwkew"
# expected = 3

class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        used = {}
        max_length = start = 0
        for index, char in enumerate(s):
            # 이미 등장했던 문자라면 'start' 위치 갱신
            if char in used and start <= used[char]:
                start = used[char] + 1
            else:  # 최대 부분 문자열 길이 갱신
                max_length = max(max_length, index - start + 1)
            # 현재 문자의 위치 삽입
            used[char] = index

        return max_length


s = Solution()
result = s.lengthOfLongestSubstring(input)
print(expected == result, result)
