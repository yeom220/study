# 금지된 단어를 제외한 가장 흔하게 등장하는 단어를 출력하라. 대소문자 구분을 하지 않으며, 구두점(마침표, 쉼표) 또한 무시한다.
import collections
import re
from typing import List

paragraph = "Bob hit a ball, the hit BALL flew far after it was hit."
banned = ["hit"]


def most_common_word(self, paragraph: str, banned: List[str]) -> str:
    words = [word for word in re.sub(r'[^\w]', ' ', paragraph).lower().split()
             if word not in banned]
    # 딕셔너리 사용
    # counts = collections.defaultdict(int)
    # for word in words:
    #     counts[word] += 1
    # return max(counts, key=counts.get)
    # Counter 객체 사용
    counts = collections.Counter(words)
    # 가장 흔하게 등장하는 단어의 첫 번째 인덱스 리턴
    return counts.most_common(1)[0][0]


print(most_common_word(paragraph, paragraph, banned))
