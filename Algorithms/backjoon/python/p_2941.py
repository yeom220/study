c_alphabet = ['c=', 'c-', 'dz=', 'd-', 'lj', 'nj', 's=', 'z=']

s = input()
c_count = 0
dz_count = 0
for c in c_alphabet:
    count = s.count(c)
    if c == 'dz=':
        dz_count = count
    c_count += ((len(c) - 1) * count)
    # print(count, c_count, dz_count)

result = len(s) - c_count + dz_count
print(result)
