# 4장 문제 풀이 
# 1번 

def odd_is(a):
    if a%2 == 0:
        return "{0}은 짝수 입니다.".format(a)
    else:
        return "{0}은 홀수 입니다.".format(a)

print(odd_is(3))

# 답안에서는 
# if a%2 == 1:
# return True
# else:
# return False 로 코드를 작성 하였다. 
