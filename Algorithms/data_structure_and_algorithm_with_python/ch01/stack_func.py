capacity = 10
array = [None] * capacity
top = -1


def is_empty():
    return top == -1


def is_full():
    return top == capacity - 1


def push(e):
    if is_full():
        print('stack overflow')
        exit()
    global top
    top += 1
    array[top] = e


def pop():
    if is_empty():
        print('stack underflow')
        exit()
    global top
    top -= 1
    return array[top + 1]


def peek():
    if is_empty():
        pass
    return array[top]


def size():
    return top + 1
