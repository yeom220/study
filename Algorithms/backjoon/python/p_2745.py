from typing import List


# chars = [chr(i+65) for i in range(26)]
# nums = [i + 10 for i in range(26)]
def degree(a: int, b: int):
    result = 1
    for _ in range(b):
        result *= a
    return result


n, b = input().split()

inputs: List[str] = list(n)
inputs = inputs[::-1]
result = 0
for i in range(len(inputs)):
    num = 0
    if inputs[i].isdigit():
        num = int(inputs[i])
    else:
        num = ord(inputs[i]) - 55

    d = degree(int(b), i)
    result += num * d

print(result)
