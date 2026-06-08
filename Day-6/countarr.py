n=int(input())

arr=[]
for i in range(n):
    num=int(input())
    arr.append(num)
    
count=0
for i in arr:
    if i>10:
        count+=1
print(count)
