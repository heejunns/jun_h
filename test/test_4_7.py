# 4장 문제풀이 
# 7번 
f = open("testttt.py", "w")
f.write(input("입력하세요:"))
f.write("\n")
f.write(input("입력하세요:"))
f.close()

f = open("testttt.py" , "r")
c = f.read()
print(c)
b = c.replace("java","python")
f.close()

f = open("testttt.py","w")
f.write(b)
f.close()