# number = int(input("Enter a number: "))
# is_prime = True
# for i in range(2, number):
#     if number % i == 0:
#         is_prime = False
# if is_prime:
#     print("It's a prime number.")
# else:
#     print("It's not a prime number.")


number = int(input('Enter a number: '))
def prime_Checker(number):
    if number/number ==1 and number/1 == number:
        print('It is a prime number.')
    else:
        print('It is not a prime number.')

prime_Checker(number)