# Python program to display all the prime numbers within an interval

def n_prime_number(lower,upper):
    for num in range(lower, upper + 1):
        # all prime numbers are greater than 1
        if num > 1:
            for i in range(2, num):
                if (num % i) == 0:
                    break
            else:
                print(num)
lower=0
upper=int(input("Enter a number"))
n_prime_number(lower,upper)
