""" 숫자 자료형 실습

int: 정수 자료형
float: 실수 자료형
complex: 실수부와 허수부를 갖는 '복소수' 자료형

"""

# type(변수명 또는 값) 함수
# - 변수 또는 값의 데이터 타입(자료형)을 확인하는 파이썬 내장 함수print(type(10))

# 정수
n = 123
print(f"n: {n} - {type(n)}")

# 자릿수 구분 _
price = 10_000_000_000 # 출력 시 _는 생략된다
print(f"price: {price} - {type(price)}") 


# 2진법, 8진법 16진법 접두어 및 출력
a = 0b100
print('0b100:', a) # 4
# 출력: 0b100: 4
b = 0o23
print('0o23:', b) # 19
# 출력: 0o23: 19
c = 0xff
print('0xff:', c) # 255
# 출력: 0xff: 255

import sys
print(sys.maxsize)
print(sys.maxsize) # 9223372036854775807

# 실수(float)
f1 = 123.456
print(f"f1: {f1} - {type(f1)}") # f1: 123.456 - <class 'float'>

# 실수를 정수로 변환(소수점 아래 버림)
print(int(f1)) # 123

# 복소수(complex)
c = 3 + 4j
print(f"c: {c} - {type(c)}") # c: (3+4j) - <class 'complex'>

# 산술 연산(사칙연산: +, -, *, /)
print('1 + 2:', 1 + 2)
# 출력: 1 + 2: 3

print('1 - 2:', 1 - 2)
# 출력: 1 - 2: -1

print('1 * 2:', 1 * 2)
# 출력: 1 * 2: 2

print('1 / 2:', 1 / 2)
# 출력: 1 / 2: 0.5

# 몫:  //
print('5 // 3:', 5 // 3)  # 1

# 나머지:  %
print('5 % 3:', 5 % 3)  # 2

# 거듭제곱: **
print(2 ** 8)
print(2 ** 10)
print(2 ** 16)
print(2 ** 32)
print(2 ** 64)