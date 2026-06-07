'''num=int(input())
fact=1
i=1
while i<=num:
    fact=fact*i
    i+=1
print("The factorial is",fact)'''




n=int(input())
fact=1
for i in range(1,n+1):
    fact=fact*i
print("The factorial is",fact)