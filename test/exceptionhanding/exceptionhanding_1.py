# 예외 처리 
try : 
    a = [1,2,3,4,5,6,7,8,8,9,10]
    print(a[3])
except (ZeroDivisionError, IndexError): # as c(오류 메세지 변수)
    print("오류")
else:
    print("이 코드에는 오류가 없습니다.")

# except 를 여러개 만들수도 있고 위에 코드처럼 발생 오류를 괄호()로 묶을수도 있다. 

