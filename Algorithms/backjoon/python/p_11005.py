def reverse_str(s):
    tmp = list(s)
    return ''.join(tmp[::-1])


n, b = map(int, input().split())
alphabet = [chr(i) for i in range(55, 65 + 26)]
answer = ''
while n > 0:
    mod = n % b
    if mod >= 10:
        answer += alphabet[mod]
    else:
        answer += str(mod)
    n = n // b

print(reverse_str(answer))
