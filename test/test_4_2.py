# 4장 문제 풀이 
# 2장 

def ad(*args):
    result = 0
    for i in args:
        result = result + i 
    return result/len(args)
print(ad(1,2,3,4,5,70,345,35))
