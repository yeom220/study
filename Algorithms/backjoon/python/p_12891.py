import sys


def add(char):
    index = -1
    if char == 'A':
        index = 0
    elif char == 'C':
        index = 1
    elif char == 'G':
        index = 2
    elif char == 'T':
        index = 3

    if index == -1:
        return
    my_arr[index] += 1
    if my_arr[index] == check_arr[index]:
        result_arr[index] = 1


def remove(char):
    index = -1
    if char == 'A':
        index = 0
    elif char == 'C':
        index = 1
    elif char == 'G':
        index = 2
    elif char == 'T':
        index = 3

    if index == -1:
        return
    if my_arr[index] == check_arr[index]:
        result_arr[index] = 0
    my_arr[index] -= 1


read = sys.stdin.readline
s, p = map(int, read().rstrip().split())
text = list(read().rstrip())
check_arr = list(map(int, read().rstrip().split()))
my_arr = [0] * 4
result_arr = [0] * 4
answer = 0

for i in range(len(check_arr)):
    if check_arr[i] == 0:
        result_arr[i] = 1

for i in range(p):
    add(text[i])
if result_arr.count(1) == 4:
    answer += 1

for i in range(p, s):
    add(text[i])
    remove(text[i - p])
    if result_arr.count(1) == 4:
        answer += 1

print(answer)
