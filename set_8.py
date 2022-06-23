# set(집합)
# 특징 : 중복 안됨, 순서 없음 , 중복을 제거하기 위한 필터로 역할로 사용. 

my_set = {1,2,3,3,3}
print(my_set) # {1,2,3} 으로 출력되고 뒤에 3은 무시된다. 

java = {"유재석", "김태호", "박명수"}
python = set(["유재석", "박명수"])
'''
# 교집합 (java와 python을 모두 할 수 있는 개발자)를 출력 
print(java&python) 
print(java and python) # &,and 는 같은 의미이다. 
print(java.intersection(python)) # intersection도 같은 뜻 이다.  
print(python.intersection(java)) # 바로 위 코드와 같은 결과를 가진다. 

# 합집합 (java도 할수 있고 python도 할 수 있는 개발자)를 출력 
print(java or python) 
print(java | python)
print(java.union(python)) # union 도 합집합을 의미한다. 
print(python.union(java)) # 바로 위 코드와 같은 결과를 가진다. 
# 차집합 (java는 할 수 있지만 python은 할 줄 모르는 개발자)를 출력 
print(java - python)
print(java.difference(python)) 

print(python - java) # 위 코드와 다른 결과를 가진다. 
print(python.difference(java))

'''
# 교육을 받아서 python을 할 줄 아는 사람이 늘어났다고 가정. 
python.add("김태호") 
print(python)

# 김태호가 java를 까먹었다고 가정하면 
java.remove("김태호") 
print(java)

java.update(["강호동","이수근"]) # 여러개의 값을 추가 할때 update 함수를 사용한다. 
print(java)


