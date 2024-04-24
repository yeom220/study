# Given an array of integers temperatures represents the daily temperatures, return an array answer such that answer[i] is the number of days you have to wait after the ith day to get a warmer temperature. If there is no future day for which this is possible, keep answer[i] == 0 instead.
from typing import List

# Example 1:
# Input: temperatures = [73,74,75,71,69,72,76,73]
# Output: [1,1,4,2,1,1,0,0]
input = [73, 74, 75, 71, 69, 72, 76, 73]
expected = [1, 1, 4, 2, 1, 1, 0, 0]


# # Example 2:
# # Input: temperatures = [30,40,50,60]
# # Output: [1,1,1,0]
# input = [30, 40, 50, 60]
# expected = [1, 1, 1, 0]

# # Example 3:
# # Input: temperatures = [30,60,90]
# # Output: [1,1,0]
# input = [30, 60, 90]
# expected = [1, 1, 0]


class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        answer = [0] * len(temperatures)
        stack = []

        for i, cur in enumerate(temperatures):
            # 현재 온도가 스택 값보다 높다면 정답 처리
            while stack and cur > temperatures[stack[-1]]:
                last = stack.pop()
                answer[last] = i - last
            stack.append(i)

        return answer


s = Solution()
result = s.dailyTemperatures(input)
print(expected == result, result)