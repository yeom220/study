attendance = [False for _ in range(31)]
for _ in range(28):
    student = int(input())
    attendance[student] = True

for i in range(1, len(attendance)):
    if not attendance[i]:
        print(i)
