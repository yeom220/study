import collections

grade = collections.defaultdict()
grade['A+'] = 4.5
grade['A0'] = 4.0
grade['B+'] = 3.5
grade['B0'] = 3.0
grade['C+'] = 2.5
grade['C0'] = 2.0
grade['D+'] = 1.5
grade['D0'] = 1.0
grade['F'] = 0.0

total = 0.0
total_p = 0.0
for _ in range(20):
    subject, point, g = input().split()
    point = float(point)
    if g == 'P':
        continue
    total += (point * grade[g])
    total_p += point

average = total / (total_p)
print(average)
