n = int(input())
if n != 1:
    half = n // 2 + 1
    checked = [0 for _ in range(half)]
    answer = []
    index = 2
    while n > 1 and index < half:
        if checked[index] == 1:
            index += 1
            continue
        if n % index == 0:
            answer.append(index)
            n //= index
        else:
            mul = 1
            while index * mul < half:
                checked[index * mul] = 1
                mul += 1
            index += 1
    if len(answer) == 0:
        print(n)
    else:
        for n in answer:
            print(n)
