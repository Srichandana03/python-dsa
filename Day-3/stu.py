marks=int(input())
sports_certificate=input("Does the student have a sports certificate? (yes/no): ")
if marks>=70 and sports_certificate=="yes":
    print("The student is eligible for the scholarship")
else:
    print("The student is not eligible for the scholarship")