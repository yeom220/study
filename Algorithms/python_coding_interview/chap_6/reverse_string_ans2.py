# 문자열을 뒤집는 함수를 작성하라. 입력값은 문자 배열이며, 리턴 없이 리스트 내부를 직접 조작하라.
from typing import List

given1 = ["h", "e", "l", "l", "o"]
then1 = ["o", "l", "l", "e", "h"]
given2 = ["H", "a", "n", "n", "a", "h"]
then2 = ["h", "a", "n", "n", "a", "H"]


# 파이썬다운 방식
def reverseString(self, s: List[str]) -> None:
    s.reverse()
    print(self)


reverseString(given1, given1)
reverseString(given2, given2)
