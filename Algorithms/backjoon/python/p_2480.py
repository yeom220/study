inputs = input().split()
inputs.sort()
dice_list = []
dice_list_size = 0
max = 0
for str in inputs:
    num = int(str)
    if num > max:
        max = num
        if dice_list_size <= 1:
            dice_list.clear()
            dice_list_size = 0
            dice_list.append(num)
            dice_list_size += 1
    elif num == max:
        dice_list.append(num)
        dice_list_size += 1

if dice_list_size == 3:
    print(10000 + dice_list[0] * 1000)
elif dice_list_size == 2:
    print(1000 + dice_list[0] * 100)
else:
    print(dice_list[0] * 100)
