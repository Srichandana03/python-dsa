n=int(input())

arr=[]

for i in range(n):
    num=int(input())
    arr.append(num)
smallest=arr[0]
for i in arr:
    if i<smallest:
        smallest=i
print(smallest)
