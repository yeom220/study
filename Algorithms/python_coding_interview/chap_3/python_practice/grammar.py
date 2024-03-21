import pprint
import sys

# 리스트 컴프리헨션 예제
# 예제 1
ex_1 = []
for n in range(1, 10 + 1):
    if n % 2 == 1:
        ex_1.append(n * 2)
print(ex_1)

# 리스트 컴프리헨션
list_comprehension_ex_1 = [n * 2 for n in range(1, 10 + 1) if n % 2 == 1]
print(list_comprehension_ex_1)

# 예제 2
original = {'a': 1, 'b': 2, 'c': 3}
ex_2 = {}
for key, value in original.items():
    ex_2[key] = value
print(ex_2)

list_comprehension_ex_2 = {key: value for key, value in original.items()}
print(list_comprehension_ex_2)


# 제너레이터 생성 방법
def get_natural_number():
    n = 0
    while True:
        n += 1
        yield n


ex_3 = get_natural_number()
print(ex_3)

g = get_natural_number()
for _ in range(0, 10):
    print(next(g))


# 제너레이터
def generator():
    yield 1
    yield 'string'
    yield True


g = generator()
print(g)
for _ in range(0, 3):
    print(next(g))

# range
print(list(range(5)))
print(range(5))
type(range(5))
for i in range(5):
    print(i, end=' ')

# 숫자 100만개 생성 차이
# 숫자가 100만개 담긴 리스트 리턴
ex1_num_1m = [n for n in range(1000000)]
# 숫자 100만개 생성 하는 range 클래스 리턴
ex2_num_1m = range(1000000)
print(len(ex1_num_1m))
print(len(ex2_num_1m))
print(ex2_num_1m == ex2_num_1m)
# print(ex1_num_1m)
print(type(ex1_num_1m))
print(ex2_num_1m)
print(type(ex2_num_1m))
# 메모리 점유율 비교
print(sys.getsizeof(ex1_num_1m))
print(sys.getsizeof(ex2_num_1m))
# 인덱스로 접근
print(ex2_num_1m[999])

# enumerate
ex_list = [1, 2, 3, 2, 45, 2, 5]
print(ex_list)
# 인덱스 자동 부여
ex_enumerate = enumerate(ex_list)
print(ex_enumerate)
print(list(ex_enumerate))
# 인덱스와 값을 출력
# ex1: 불필요한 list[i] 조회 작업
ex2_list = ['a1', 'b2', 'c3']
for i in range(len(ex2_list)):
    print(i, ex2_list[i])
# ex2: 인덱스를 위한 변수를 별도 관리 해야함
i = 0
for v in ex2_list:
    print(i, v)
    i += 1
# ex3: 깔끔하게 enumerate()를 활용
for i, v in enumerate(ex2_list):
    print(i, v)

# 나눗셈 연산자
# 파이썬 3+ 에선 타입 자동 변경 (int -> float)
ex1_divide = 5 / 3
print(ex1_divide)
print(type(ex1_divide))
# 파이썬 2 이하 에선 정수 타입 유지 (파이썬 3+ '//'연산자와 파이썬 2 '/'연산자는 동일한 역할)
print(5 // 3)
print(type(5 // 3))
# 나머지 연산자
print(5 % 3)
# 몫과 나머지 구하는 함수
print(divmod(5, 3))

# print
# ',' 구분자 공백으로 출력
print('A1', 'B1')
# sep 파라미터로 구분자 변경
print('A1', 'B2', 'C3', sep=',')
# end 파라미터로 줄 바꿈 제한
for i in range(2):
    print(i, end=' ')
# 리스트 출력할 때는 join()으로 묶어서 처리
print()
ex1_join_list = ['A', 'B', 'C']
print(' '.join(ex1_join_list))
# 두개의 변수를 함께 출력하는 방법
idx = 1
fruit = 'Apple'
print('{0}: {1}'.format(idx + 1, fruit))
# 인덱스 생략도 가능
print('{}: {}'.format(idx + 1, fruit))
# 가장 추천하는 방법은 f-string(formated string literal). 단, 파이썬 3.6+ 지원
print(f'{idx + 1}: {fruit}')


# pass
# 널 연산. 목업(mockup) 인터페이스 구현할 때 불필요한 에러를 방지.
class MyClass(object):
    def method_a(self):
        # pass가 없는 경우 method_b()에서 인덴트 오류 발생
        pass

    def method_b(self):
        print("Method B")


print(MyClass())

# locals
# 로컬 심볼 테이블 딕셔너리를 가져오는 메소드.
# 로컬에 선언된 모든 변수를 조회할 수 있다.
# 클래스 메소드 내부의 모든 로컬 변수를 출력해주어 디버깅에 많이 도움된다.
pprint.pprint(locals()) # pprint로 가독성 좋게 줄바꿈하여 출력

