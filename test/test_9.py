a = dict()
print(a)
# 점프 투 파이썬 연습문제 풀기 
# 9번 
# 다음중 오류가 발생하는 것을 고르고 그 이유를 설명하시오. 
#a['name'] = "python"
#a[('a',)] = "python"
#a[['a']] = "python" # 에러 발생 
a[250] = "python"
print(a)
# key 값은 변경이 불가능한데 리스트로 key 값이 저장되면 오류가 발생 한다.  
