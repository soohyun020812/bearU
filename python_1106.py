# 함수 (Function)
# f-string
# 문자와 변수를 혼재하여 문자열로 바꾸고 싶을 때
print(f"{3} abcd")
'''
def 함수이름(매개변수) :
    return 반환 값
'''

def 더하기(첫번째, 두번째) :
    return 첫번째+두번째
print(더하기(3, 4))

'''
출근 하시면 아침 업무로
배달 온 상자안에 물건을 전부 꺼내서
사과는 냉장실에
아이스크림은 냉동실에
그 외 나머지는 폐기처분 해주세요.
'''

def 아침업무(상자) : 
    for 물건 in 상자 :
        if 물건 == "사과" :
            print(f"'{물건}' 냉장실에 넣기")
        elif 물건 == "아이스크림" :
            print(f"'{물건}' 냉동실에 넣기")
        else :
            print(f"'{물건}' 폐기처분 하기")
출근 = True

if 출근 : 
    상자 = ["콩", "콩", "콩", "사과"]
    아침업무(상자)

# 클래스 (Class)
'''
class 클래스() :
    변수 = 1
or
class 클래스() :
    def __init__(self) : 
        self.변수 = 1

    def 변수변경(self) : 
        self.변수 = 3
'''

'''
모든 사원들은 각자
출근 하시면 아침 업무로
배달 온 상자안에 물건을 전부 꺼내서
사과는 냉장실에
아이스크림은 냉동실에
그 외 나머지는 폐기처분 해주세요.
그리고 나서 아침업무 체크 해주세요
'''

class 업무() :
    아침업무유무 = False
    
    def 아침업무유무 = True
    
    def 아침업무(self, 상자) : 
    for 물건 in 상자 :
        if 물건 == "사과" :
            print(f"'{물건}' 냉장실에 넣기")
        elif 물건 == "아이스크림" :
            print(f"'{물건}' 냉동실에 넣기")
        else :
            print(f"'{물건}' 폐기처분 하기")
    self.아침업무체크()
출근 = True

if 출근 : 
    상자 = ["콩", "콩", "콩", "사과"]

    soo_업무 = 업무()
    soo_업무.아침업무(상자)