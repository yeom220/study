a = input()
b = input()
c = int(a) * int(b)
nums = []
for n in b:
    nums.append(int(a) * int(n))
nums.reverse()
for n in nums:
    print(n)
print(c)
