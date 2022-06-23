# 계산기의 더하기 기능 
result = 0 
def add(a):
    result = 0 # 이렇게 쓰지 않으려면 globa result를 사용하면 된다. 
    result = result +  a
    return result 
print(add(3))
print(add(5))
print(add(456))
print(result) # 얘는 바깥에 있는 result이고 출력은 0이 된다. 
