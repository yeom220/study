# You're given strings jewels representing the types of stones that are jewels, and stones representing the stones you have. Each character in stones is a type of stone you have. You want to know how many of the stones you have are also jewels.
#
# Letters are case sensitive, so "a" is considered a different type of stone from "A".
import collections

# Example 1:
# Input: jewels = "aA", stones = "aAAbbbb"
# Output: 3
jewels = "aA"
stones = "aAAbbbb"
expected = 3

# # Example 2:
# # Input: jewels = "z", stones = "ZZ"
# # Output: 0
# jewels = "z"
# stones = "ZZ"
# expected = 0

class Solution:
    def numJewelsInStones(self, jewels: str, stones: str) -> int:
        # # 1. 해시 테이블을 이용한 풀이
        # freqs = {}
        # count = 0
        #
        # # 돌의 빈도 수 계산
        # for char in stones:
        #     if char not in freqs:
        #         freqs[char] = 1
        #     else:
        #         freqs[char] += 1
        #
        # # 보석의 빈도 수 합산
        # for char in jewels:
        #     if char in freqs:
        #         count += freqs[char]
        #
        # return count

        # #2. defaultdict를 이용한 비교 생략
        # freqs = collections.defaultdict(int)
        # count = 0
        #
        # # 비교 없이 돌 빈도 수 계산
        # for char in stones:
        #     freqs[char] += 1
        #
        # # 비교 없이 보석 빈도 수 합산
        # for char in jewels:
        #     count += freqs[char]
        #
        # return count

        # #3. Counter로 계산 생략
        # freqs = collections.Counter(stones) # 돌 빈도 수 계산
        # count = 0
        #
        # # 비교 없이 보석 빈도 수 합산
        # for char in jewels:
        #     count += freqs[char]
        #
        # return count

        #4. 파이썬다운 방식
        return sum(s in jewels for s in stones) # 리스트 컴프리헨션


s = Solution()
result = s.numJewelsInStones(jewels, stones)
print(expected == result, result)