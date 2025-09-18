#simple calculator in python
def calculator():
    print("---simple calculator in python---")
    print("select operations:")
    print("1.addition(+)")
    print("2.substraction(-)")
    print("3.multiplication(*)")
    print("4,division(/)")
    choice=input("enter choice(1/2/3/4):")
    
    num1=float(input("enter first number:"))
    num2=float(input("enter second number:"))

    if choice=='1':
        print(f"the result:{num1+num2}")
    elif choice=='2':
        print(f"the result:{num1-num2}")
    elif choice=='3':
        print(f"the result:{num1*num2}")
    elif choice=='4':
        if num2!=0:
            print(f"the result:{ num1/num2}")
        else:
            print("error:division by zero is not possible")
    else:
        ("invalid input")
calculator()
 
