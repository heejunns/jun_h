# 5장 문제풀이 
# 6번 
print(list(map(lambda x : x*3, [1,2,3,4])))

# 만약 map함수를 몰랐다면? for 을 사용해야 한다. 
def add(x):
    result = []
    for i in x:
        result.append(i*3)
    return result 

print(add([1,2,3,4])) 

# 이런식으로 map함수를 사용하면 한줄에 해결 가능한 것을 6줄이나 코드를 작성해야 한다. 
