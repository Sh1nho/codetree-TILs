n = int(input())  
m = list(map(int, input().split())) 

count = 0  # 2의 등장 횟수 저장

for index in range(n):
    if m[index] == 2:
        count += 1
        if count == 3:
            print(index + 1) 
            break  
    
