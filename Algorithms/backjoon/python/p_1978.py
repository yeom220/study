n = input()
answers = [0 for _ in range(1001)]
list = list(map(int, input().split()))

for num in list:
    count = 0
    for i in range(1, num // 2 + 1):
        if num % i == 0:
            count += 1
        if count > 1:
            break

    if count == 1:
        answers[num] = 1

print(answers.count(1))
