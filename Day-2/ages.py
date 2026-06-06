age=int(input())
if age<10:
    print("You are a child")
elif age>=13 and age<17:
    print("You are a teenager")
elif age>=18 and age<60:
    print("You are an adult")
elif age>=60:
    print("You are a senior citizen")
else:
    print("You are a kid")
