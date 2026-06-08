n=int(input())
arr=[]
largest=0
for i in range(n):
    num=int(input())
    arr.append(num)
for i in arr:
    if i>largest:
        largest=i
print(largest)
