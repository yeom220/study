from ch01.stack_class import ArrayStack


def check_brackets(statement):
    stack = ArrayStack(100)
    left_brackets = ['(', '{', '[']
    right_brackets = [')', '}', ']']
    for ch in statement:
        if ch in left_brackets:
            stack.push(ch)
        elif ch in right_brackets:
            if stack.is_empty():
                return False
            else:
                left = stack.pop()
                if ch == right_brackets[0] and left != left_brackets[0]:
                    return False
                elif ch == right_brackets[1] and left != left_brackets[1]:
                    return False
                elif ch == right_brackets[2] and left != left_brackets[2]:
                    return False
    return stack.is_empty()


if __name__ == '__main__':
    print(check_brackets(input('입력: ')))
