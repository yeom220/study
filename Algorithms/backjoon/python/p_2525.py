hour, min = map(int, input().split())
cook = int(input())
condition = (min + cook) > 59
if condition:
    hour += (min + cook) / 60
    min = (min + cook) % 60
else:
    min += cook
if hour > 23:
    hour = hour % 24
print("{} {}".format(int(hour), min))
