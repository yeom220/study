def print_reverse(msg, len):
    if len > 0:
        print(msg[len-1], end='')
        print_reverse(msg, len-1)


print_reverse('hello', len('hello'))
