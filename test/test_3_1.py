# 3장 연습문제 풀이 
# 1번 
a = "life is too short, you need python"

if "wife" in a: print("wife")
elif "python" in a and "you" not in a : print(":python")
elif "shirt" not in a: print("shirt")
elif "need" in a: print("need")
else: print("none")

# 결과 값은 어떻게 될 것인가?
# shirt 7번째 줄이 참이 되어 shirt 를 출력 하고 if 문을 탈출 한다. 
