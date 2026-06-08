n=int(input())
arr=[]

for i in range(n):
    num=int(input())
    arr.append(num)
even_count=0
for i in arr:
    if i%2==0:
        even_count+=1
print(even_count)