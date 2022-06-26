a = input()
x = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
total = 0 
total_str = ["A"]  
for i in a:    
    if int(x.find(i))>int(x.find(total_str[0])):  # 오른쪽으로 움직이는 방법 
        right_total = int(x.find(i)) - int(x.find(total_str[0]))      
    else:
        right_total = ((int(x.find("Z")) - int(x.find(total_str[0])) ) + ( int(x.find(i)) - int(x.find("A")))) +1
        
    if int(x.find(i)) > int(x.find(total_str[0])): # 왼쪽으로 움직이는 방법
        left_total =  (int(x.find(total_str[0])) - int(x.find("A")) ) + ( int(x.find("Z")) - int(x.find(i)))  +1
    else:
        left_total =  int(x.find(total_str[0]))-int(x.find(i)) 

    if right_total > left_total: # 최소값 찾기
        total +=left_total 
        total_str.pop()
        total_str.append(i)
    else:
        total += right_total
        total_str.pop()
        total_str.append(i)

print(total)
