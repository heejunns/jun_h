# 4장 문제풀이 
# 3번 
def add():
    input1 = int(input("첫번째 숫자를 입력하세요:"))
    input2 = int(input("두번째 숫자를 입력하세요:"))
    total = input1 + input2
    return "두 수의 합은 %d 입니다." % total
print(add())
# 문제에서 있는 그래도 코드를 작성하게 되면 input 은 문자열로 입력되기 때문에 input1 에서 3을 입력하고 
# input2에서 6을 입력하면 결과 total 값은 36 이 출력된다. 
# input에 입력하는 숫자를 숫자로 입력하려면 input함수를 int 로 감싸줘야 한다. 
# 감싸주게 되면 9가 나온다. 