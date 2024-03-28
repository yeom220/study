# 주어진 문자열이 팰린드롬인지 확인하라. 대소문자를 구분하지 않으며, 영문자와 숫자만을 대상으로 한다.
# 팰린드롬(Palindrome): 앞뒤가 똑같은 단어나 문장으로, 뒤집어도 같은 말이 되는 단어 또는 문장이다.
import collections
import re
from typing import Deque

given1 = 'A man, a plan, a canal: Panama'
expected1 = True
given2 = 'race a car'
expected2 = False
# 슬라이싱 사용한 풀이
def isPalindrome(self, s: str) -> bool:
    s = s.lower()
    # 정규식으로 불필요한 문자 필터링
    s = re.sub('[^a-z0-9]', '', s)
    return s == s[::-1] # 슬라이싱

print(isPalindrome(given2, given2))