# 5장 문제풀이 
# 13번 
import random
print("요번주 로또 당첨 번호는:"+str(random.sample(list(range(1,46)),6)))

print(range(5))
print(list(range(5)))
print(set(range(5)))
print(tuple(range(5)))

# 만약 sample 함수를 모른다면 어떻게 코드를 작성해야 할까?
result = [] 
while len(result) < 6:
    a = random.randint(1,46)
    if a not in result:
        result.append(a)

print("요번주 로또 당첨 번호는:"+str(result))

# for 을 사용해서 하는 방법 
result = []
a = list(range(1,46))
print(a)
random.shuffle(a) 
for i in a:
    result.append(i)
    a.pop(i)
    if len(result) == 6:
        break
print("요번주 로또 당첨 번호는:"+str(result))

# 이런식으로도 코드 작성이 가능하다. 하지만 매우 비효율 적이다. 
