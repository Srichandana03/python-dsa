n=int(input())

arr=[]
for i in range(n):
    num=int(input())
    arr.append(num)
total=0
for i in arr:
    total+=i
avg=total/n
print(avg)