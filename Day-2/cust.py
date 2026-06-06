amount=int(input())
if amount>=5000:
    discount=amount*0.2
    final_amount=amount-discount

    print("The final amount after discount is",final_amount)
else:
    print("No discount applicable. The final amount is",amount)