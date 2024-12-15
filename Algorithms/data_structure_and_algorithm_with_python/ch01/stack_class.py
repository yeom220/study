class ArrayStack:
    def __init__(self, capacity):
        self.capacity = capacity
        self.array = [None] * self.capacity
        self.top = -1

    def is_empty(self):
        return self.top == -1

    def is_full(self):
        return self.top == self.capacity - 1

    def push(self, e):
        if self.is_full():
            print('stack overflow')
            exit()
        self.top += 1
        self.array[self.top] = e

    def pop(self):
        if self.is_empty():
            print('stack underflow')
            exit()
        self.top -= 1
        return self.array[self.top + 1]

    def peek(self):
        if self.is_empty():
            pass
        return self.array[self.top]

    def size(self):
        return self.top + 1


if __name__ == '__main__':
    s = ArrayStack(100)

    msg = input('입력: ')
    for c in msg:
        s.push(c)

    print('출력: ', end='')
    while not s.is_empty():
        print(s.pop(), end='')
