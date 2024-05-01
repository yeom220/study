# # 풀이 1
# dic = {
#     'ABC':2,
#     'DEF':3,
#     'GHI':4,
#     'JKL':5,
#     'MNO':6,
#     'PQRS':7,
#     'TUV':8,
#     'WXYZ':9,
# }
#
# time = [i + 1 for i in range(10)]
#
# s = input()
# result = 0
# for c in s:
#     for k in dic.keys():
#         if c in k:
#             result += time[dic[k]]
#             break
#
# print(result)

# 풀이 2
arr = [''] * 10
arr[2], arr[3], arr[4], arr[5], arr[6], arr[7], arr[8], arr[9] \
    = 'ABC', 'DEF', 'GHI', 'JKL', 'MNO', 'PQRS', 'TUV', 'WXYZ'
result = 0

for c in input():
    for i in range(2, len(arr)):
        if c in arr[i]:
            result += i + 1
            break

print(result)
