# 6장 - 2
# 10 미만의 자연수에서 3과 5의 배수를 구하면 3,5,6,9이다. 이들의 총합은 23이다. 
# 1000 미만의 자연수에서 3의 배수와 5의 배수의 총합을 구하라. 
# 일단 range 함수로 1 부터 999까지 리스트로 생성하고 for 문으로 요소 하나씩 if 문이나 while 문으로 
# 3과 5의 배수를 판별하여 reduce 함수로 모든 요소를 합쳐버리기.
from functools import reduce
def add(x):
    result = []
    for i in x:
        if i%3 == 0 or i%5 == 0 :
            result.append(i)
    return result
a = add(list(range(1,1000)))
print(reduce(lambda x,y: x+y,a))

# 위에 add 함수도 filter 로 대체 할 수 있다. 
a = list(filter(lambda x : x%3==0 or x%5 == 0 ,list(range(1,1000))))
print(reduce(lambda x,y: x+y ,a))
# 두줄로도 가능하다. 

def add(x,y):
    return x+y
print(reduce(add, [1,2,3,4,5]))

# reduce 를 사용하지 않으면 
def addddd(x):
    result = 0 
    for i in x:
        result += i 
    return result 

print(addddd(list(range(1,6))))

# 또는
def addd(x,y):
    return x+y 

result = 0 
for i in list(range(1,6)):
    result = addd(result,i)

print(result)

################################### 점프 투 파이썬 풀이에서는 #################### 
result = 0 
for i in list(range(1,1000)):
    if i%3 == 0 or i%5 == 0 :
        result += i 
print(result)

# 함수를 사용하는 것보다 이런식으로 바로 더하는게 나은거 같다 . 
# 나는 애초에 3,5 의 배수의 값을 리스트 값으로 만든 후에 reduce 함수로 모든 요소를 더했는데 
# 하는것보다는 위에 코드처럼 바로 3,5의 배수의 값이 나오면 바로 더하여 총 값을 만드는 것이 
# 더 효율적인 것 같다. 하지만 가장 짧게 코드를 작성하는 방법은 
a = list(filter(lambda x:x%3==0 or x%5==0,list(range(1,1000))))
print(reduce(lambda x,y: x+y,a))
# 로 두줄로 같은 결과를 얻을 수 있는 방법이 있다. 