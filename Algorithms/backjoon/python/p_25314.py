N = int(input())
result: str = 'int'
for i in range(0, N, 4):
    result = 'long ' + result
print(result)
