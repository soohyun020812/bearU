# 주석 쓰는 방법 1
'''
주석 쓰는 방법 2
'''
# print("터미널에 출력하게 만들어 프로그램의 현황상황을 확인 = 디버깅")

# 변수 (Variable)
var = 4
print(var)
# 변수 재할당 가능
'''
변수에 들어갈 수 있는 것
정수 = 2
실수 = 1.5
글자 = "글자"
불 = True(1) or False(0)
사전 = {"키" : "값"}
튜플 = () 내부 값 변경 불가능
리스트 = [] 내부 값 변경 가능
'''
# ex
사전 = {"월":"11월", "일":"5일"}
print(사전)
print(사전["일"])

# 조건문 (Conditional)
'''
if 조건 :
    코드
elif 조건 :
    코드
else :
    코드
'''
# 조건문은 비교 연산자나 조건 연산자와 함께 많이 쓰임
'''
- 비교연산자
값 == 값 : 양쪽의 값이 서로 같다
값 != 값 : 양쪽의 값이 서로 다르다
값 > 값, 값 < 값, 값 >= 값, 값 <= 값 : 양쪽 값 크기 비교

- 조건연산자
1조건 and 2조건 : 1조건이 만족하면서 2조건 만족
1조건 or 2조건 : 1조건 2조건 중 하나만 만족해도 만족
'''
# ex
a = 3
b = 5
if a == 3:
    print("in")

print(a == 3) #True
print(a == b) # False
print(a == 3 or b != 5)  # True
print(a == 3 and b != 5) # False

# 반복문 (Iteration)
'''
for 값 in 리스트:
    코드
'''
# ex
상자 = ["사과", "배", "콩", "두부"]
for 값 in 상자 :
    print(값)