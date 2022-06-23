# 4장 문제풀이 
# 6번 
f = open("testtt.py", "w")
f.write(input("입력하세요:"))
f.close()
f = open("testtt.py", "a")
f.write(input("추가적으로 입력하세요:"))
f.close()