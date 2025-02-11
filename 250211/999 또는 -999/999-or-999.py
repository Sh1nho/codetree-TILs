k = []

while True:
    a = input().split()
    
    for num in a:
        num = int(num)  
        if num == -999 or num == 999:
            print(max(k), min(k))  
            exit()  
        k.append(num) 
