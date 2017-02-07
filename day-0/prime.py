# a function to generate prime numbers

prime_numbers = 0  # initialising


# function declaration
def is_prime_number(x):
    if x >= 2:
        for y in range(2, x):
            if not (x % y):
                return False
    else:
        return False
    return True

# for loop to get all the prime numbers
for i in range(int(input("Input maximum number: "))):
    if is_prime_number(i):
        prime_numbers += 1
        print(i)

# print statement
print("there are " + str(prime_numbers) + " prime numbers.")
