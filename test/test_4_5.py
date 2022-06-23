# 4장 문제풀이 
# 5번 
f1 = open("testt.py", "w")
f1.write("Life is too short!")
f1.close()

f2 = open("testt.py","r")
c = f2.read()
print(c)
f2.close()
# close()함수로 닫지 않은 상태에서 다시 열면 데이터를 읽을 수 없다. 닫아준 후 다시 열어서 파일의 
# 내용을 읽어야 한다. 
# with open("testt.py","w") as f1: 사용하면 clcose() 함수를 사용하지 않아도 된다. 