# 주어진 문자열이 팰린드롬인지 확인하라. 대소문자를 구분하지 않으며, 영문자와 숫자만을 대상으로 한다.
# 팰린드롬(Palindrome): 앞뒤가 똑같은 단어나 문장으로, 뒤집어도 같은 말이 되는 단어 또는 문장이다.

given1 = 'A man, a plan, a canal: Panama'
expected1 = True
given2 = 'race a car'
expected2 = False

# 리스트 변환 풀이
def isPalindrome(self, s: str) -> bool:
    strs = []
    for char in s:
        if char.isalnum():  # char.isalnum(): 영문자, 숫자 여부 판별 함수
            strs.append(char.lower())  # char.lower(): 소문자로 변환 함수
    # 팰린드롬 여부 판별
    while len(strs) > 1:
        if strs.pop(0) != strs.pop():
            return False

    return True


print(isPalindrome(given2, given2))
