# Given a string s, remove duplicate letters so that every letter appears once and only once. You must make sure your result is
# the smallest in lexicographical order
#  among all possible results.
import collections

# # Example 1:
# # Input: s = "bcabc"
# # Output: "abc"
# input = "bcabc"
# expected = "abc"

# Example 2:
# Input: s = "cbacdcbc"
# Output: "acdb"
input = "cbacdcbc"
expected = "acdb"


class Solution:
    def removeDuplicateLetters(self, s: str) -> str:
        # # 1.재귀를 이용한 분리
        # # 집합으로 정렬
        # for char in sorted(set(s)):
        #     suffix = s[s.index(char):]
        #     # 전체 집합과 접미사 집합이 일치할 때 분리 진행
        #     if set(s) == set(suffix):
        #         return char + self.removeDuplicateLetters(suffix.replace(char, ''))
        # return ''

        # 2.스택을 이용한 문자 제거
        counter, seen, stack = collections.Counter(s), set(), []

        for c in s:
            counter[c] -= 1
            if c in seen:
                continue
            # 뒤에 붙일 문자가 남아 있다면 스택에서 제거
            while stack and c < stack[-1] and counter[stack[-1]] > 0:
                seen.remove(stack.pop())
            stack.append(c)
            seen.add(c)

        return ''.join(stack)


s = Solution()
result = s.removeDuplicateLetters(input)
print(expected == result, result)
