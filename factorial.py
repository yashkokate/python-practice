def factorial(num):
    factorial=1
    if num<0:
        print("Factorial does not exist")
    elif num==0:
        print(factorial)
    else:
        for i in range(1,num+1):
            factorial=factorial*i
        print(factorial)

num=int(input("Enter a number"))
factorial(num)
        