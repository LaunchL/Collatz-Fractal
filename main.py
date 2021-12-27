#       Collatz Fractal By Lab
#Discord - https://discord.gg/ngMUeFEgQa, GitHub - https://github.com/LaunchL.
#Imports


#Code
print("Welcome to Callatz Fractals. This program tells about a hypothesis of a problem that cannot be solved!")
n = int(input("Enter any integer greater than 0: "))
if(n == 0):
    n = int(input("An integer greater than 0: "))

if(n % 2 == 0):
    n = n / 2
    print(n)
else:
    n = n * 3 + 1
    print(n)

if(n % 2 == 0):
    n = n / 2
    print(n)
else:
    n = n * 3 + 1
    print(n)

if(n % 2 == 0):
    n = n / 2
    print(n)
else:
    n = n * 3 + 1
    print(n)

if(n == 4, 2, 1):
    n = int(input("Your number fell into loop 4, 2, 1. Enter a new number: "))

if(n % 2 == 0):
    n = n / 2
    print(n)
else:
    n = n * 3 + 1
    print(n)

if(n % 2 == 0):
    n = n / 2
    print(n)
else:
    n = n * 3 + 1
    print(n)

if(n % 2 == 0):
    n = n / 2
    print(n)
else:
    n = n * 3 + 1
    print(n)

print("That's all! You yourself can continue to calculate the numbers. Made by Lab. Bye!")
print("Discord - https://discord.gg/ngMUeFEgQa, GitHub - https://github.com/LaunchL.")
