def switch_number(num: str):
    list = [i for i in num]
    list[0], list[2] = list[2], list[0]
    return int(''.join(list))


a, b = input().split()
a, b = switch_number(a), switch_number(b)
print(max(a, b))
