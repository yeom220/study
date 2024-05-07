import collections

s_list = list(input())
dic = collections.defaultdict(int)
for c in s_list:
    dic[c.capitalize()] += 1

max = 0
letter = ''
for k in dic.keys():
    v = dic[k]
    if v > max:
        max = v
        letter = k
    elif v == max:
        letter = '?'

print(letter)
