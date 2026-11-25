# 출력
print("[출력]")

a = 5
b = 3
print(a + b) # 변수를 이용한 연산과 출력 가능

print("5 + 3 = 8") # 출력 목표

print(a, "+", b, "=", (a+b))

# f-string 
# - 작성법:  f"문자열 {변수}"  
# 변수 값을 문자열에 포함
print(f"{a} + {b} = {a+b}")

# 입력
print("[입력]")
name = input("이름을 입력하세요: ")
print(f"안녕하세요, {name}님!")
