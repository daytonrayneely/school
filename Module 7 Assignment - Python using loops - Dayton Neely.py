# numbers: list holding the 15 whole numbers to evaluate
numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15]

# number: placeholder variable that holds the current item from the list
# on each pass through the for loop
for number in numbers:
    # The % (modulus) operator gives the remainder after dividing by 2.
    # A remainder of 0 means the number divides evenly, so it is even.
    if (number % 2 == 0):
        # str(number) converts the number to text so it can be joined
        # with the rest of the message in one print statement
        print(str(number) + " is even")
    else:
        # Any remainder other than 0 means the number is odd
        print(str(number) + " is odd")
