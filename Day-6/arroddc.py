n=int(input())
arr=[]
for i in range(n):
    num=int(input())
    arr.append(num)
odd_count=0

for i in arr:
    if i%2!=0:
        odd_count+=1
print(odd_count)