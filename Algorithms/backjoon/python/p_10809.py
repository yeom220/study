s: str = input()
alphabet = [ord('a') + i for i in range(26)]
# 1
for c in alphabet:
    isFind = False
    for i in range(len(s)):
        if s[i] == chr(c):
            isFind = True
            print(i, end=' ')
            break
    if not isFind:
        print('-1', end=' ')

# 2
for c in alphabet:
    if chr(c) in s:
        print(s.index(chr(c)), end=' ')
    else:
        print('-1', end=' ')
