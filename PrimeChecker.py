def prime_checker(number):
    if number > 1:
        for i in range(2, number):
            if number % i == 0:
                print(f"The number {number} is not a prime number")
                break
        else:
            print(f"The number {number} is a prime")
    else:
        print(f"The number {number} is not a prime number")

n = int(input("Check this number: "))
prime_checker(number=n)
