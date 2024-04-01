hour, min = map(int, input().split())
minus = 45
condition = min - minus
if condition >= 0:
    print("{} {}".format(hour, min - 45))
else:
    min = condition + 60
    hour -= 1
    if hour < 0:
        hour += 24
        print("{0} {1}".format(hour, min))
    else:
        print("{} {}".format(hour, min))
