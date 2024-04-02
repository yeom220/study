# 문자열 배열을 받아 애너그램 단위로 그룹핑하라.
import collections
from typing import List

strs = ["eat", "tea", "tan", "ate", "nat", "bat"]
expected = [["bat"], ["nat", "tan"], ["ate", "eat", "tea"]]


def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
    anagrams = collections.defaultdict(list)
    for word in strs:
        # 정렬하여 딕셔너리에 추가
        anagrams[''.join(sorted(word))].append(word)
    return anagrams.values()


print(groupAnagrams(strs, strs))
