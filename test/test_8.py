# 점프 투 파이썬 연습문제 풀기 
# 8번 
# (1,2,3) 튜플에 4를 추가하여 (1,2,3,4) 만들기 
a = 1,2,3
print(a)
# 1번째 방법 자료형을 리스트로 변경하여 4를 추가하고 다시 튜플로 바꾸기 
a = list(a)
a.append(4)
print(a)
a = tuple(a)
print(a)
# 2번째 방법 
a = a+(4,)
print(a)
# 이 방법은 새로운 a 라는 튜플을 생성하는 것이다. 


