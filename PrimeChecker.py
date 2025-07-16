def prime_checker(number):
    if number > 1:
       # Check divisibility from 2 to √number (inclusive)
       # Logic: if a divisor > √n exists, its corresponding pair will be < √n
       # Therefore, checking up to √n is sufficient to find all divisors
        for i in range(2, int(number**0.5) + 1):
            if number % i == 0:
                # If remainder is 0, we found a divisor
                print(f"The number {number} is not a prime number")
                break
        else:
            print(f"The number {number} is a prime")
    else:
        print(f"The number {number} is not a prime number")

n = int(input("Check this number: "))
prime_checker(number=n)
