n=int(input())
i=2
while i<n:
    if n%i==0:
        print("Not prime")
        break
    i+=1
else:
    if n>1:
        print("Prime")
    else:
        print("Not prime")
