import sys

while True:
    inputs = sys.stdin.readline()
    if inputs == '':
        break
    a, b = map(int, inputs.split())
    print(a + b)
