# # 오류 회피하기 
try: 
    f = open("나없는파일","r")
except FileNotFoundError:
    pass
# 프로그래밍을 하다 보면 특정 오류가 발생할 경우 그냥 통과시켜야 하는 경우가 있는데 이때 
# 특정 오류가 발생하면 pass 를 사용하여 특정 오류를 회피 할 수 있다. 