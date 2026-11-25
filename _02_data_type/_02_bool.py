""" bool과 조건 조합

- boolean은 참/거짓을 나타냄.

- python에서는 "bool" 이라고 표현

- 참(True),  거짓(False)

- 주로 조건에 따른 코드 분기에 많이 사용
"""

is_true = True
is_false = False

print("is_true: ", is_true, type(is_true))
print("is_false: ", is_false, type(is_false))

# 비교 연산자
# >, <, >=, <= ==, !=

print("1 > 0.5:", 1 > 0.5)
print("1 < 0.5:", 1 < 0.5)
print("1 >= 0.5:", 1 >= 0.5)
print("1 <= 0.5:", 1 <= 0.5)
print("1 == 1:", 1 == 1)
print("1 != 1:", 1 != 1)

# 논리 부정 연산자  (! => not)
print(True)
print(not True)

# 논리 연산자: and, or

# and 연산자
# - 좌항과 우항이 모두 참(True)일때만 참
# T and T -> T
# T and F -> F
# F and T -> F
# F and F -> F

print("--- and ---")
print("100 > 0 and 1 == 1:", 100 > 0 and 1 == 1)  # True
print("30 > 20 and 123 != 123:", 30 > 20 and 123 != 123) # False
print("3 <= -3 and 12 == 12:", 3 <= -3 and 12 == 12) # False

print("9 >= 9 / 9 * 9 and 12 != 11 + 1:", 9 >= 9 / 9 * 9 and 12 != 11 + 1)

# or 연산자
# - 좌항과 우항이 모두 거짓(False)일때만 거짓
# T or T -> T
# T or F -> T
# F or T -> T
# F or F -> F

print("100 > 0 or 1 == 1:", 100 > 0 or 1 == 1) 
print("10 * 10 == 100 or 1 != 1:", 10 * 10 == 100 or 1 != 1)
print("100 == 0 or 10 == 10:", 100 == 0 or 10 == 10)
print("100 - 1000 > 0 or 23 != 20 + 3:", 100 - 1000 > 0 or 23 != 20 + 3) 

print("--- 합격 또는 불합격 여부 판별하기 ---")
# 조건 : 각 과목 점수가 40점 이상, 평균 60점 이상만 True, 나머진 False

kor = 70
eng = 50

result = kor >= 40 and eng >= 40 and (kor + eng) / 2 >= 60  # True / False가 되도록 연산 작성

print("합격여부: ", result)

print ("합격" if result else '불합격')


# 논리 연산자(not, and, or), 비교 연산자(>, <, >=, <=, ==, !=)의 결과는
# 항상 자료형이 bool 이다
