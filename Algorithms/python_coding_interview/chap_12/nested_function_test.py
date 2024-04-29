# 중첩 함수 동작 테스트
from typing import List


# 1. 내부 함수에서 부모 함수 변수 접근하는 경우
def outer_func1(t: str):
    text: str = t

    def inner_fuc():
        print(text)

    inner_fuc()


# 2. 중첩 함수에서 부모 함수에서 선언한 변수를 연산자로 조작하는 경우
def outer_func2(a: List[int]):
    b: List[int] = a
    print(id(b), b)

    def inner_fuc1():
        b.append(4)
        print(id(b), b)

    def inner_fuc2():
        print(id(b), b)

    inner_fuc1()
    inner_fuc2()


#3. 재할당으로 참조 ID 변경되는 경우
def outer_func3(t: str):
    text: str = t
    print(id(text), text)

    def inner_func1():
        text = 'World!'
        print(id(text), text)

    def inner_func2():
        print(id(text), text)

    inner_func1()
    inner_func2()


outer_func1('Python')
print('----')
outer_func2([1, 2, 3])
print('----')
outer_func3('Hello!')