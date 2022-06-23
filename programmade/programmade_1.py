# 구구단 프로그램 만들어 보기 
def mul(number):
    # number = int(input("구구단 몇단을 알고 싶으세요?"))  # 입력도 가능 
    a = tuple(range(1,10))
    for i in a:
        result = number *i 
        print(str(number)+"x"+str(i)+"="+str(result))

print(mul(int(input("구구단 몇단을 알고 싶으세요?"))))