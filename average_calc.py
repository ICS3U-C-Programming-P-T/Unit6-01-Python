#!/usr/bin/env python3
# Created by: Patrick Tumbaga
# Created on: 12/20/2025
# This program calculates the average of 10 random integers between 1 and 100

# Import the random module so we can generate random numbers
import random

# The total number of values that will be stored in the list
MAX_ARRAY_SIZE = 10

# The minimum possible random number
MIN_NUM = 1

# The maximum possible random number
MAX_NUM = 100


def main():
    # Create an empty list to store the random integers this list will eventually contain 10 numbers
    list_of_int = []

    # This variable will be used to store the sum of all the numbers in the list
    total = 0

    # Generate random numbers and store them in the list
    for i in range(MAX_ARRAY_SIZE):
        # Generate a random integer between MIN_NUM and MAX_NUM
        number = random.randint(MIN_NUM, MAX_NUM)

        # Add the random number to the list
        list_of_int.append(number)

    # Display the numbers stored in the list
    print("Generated numbers:")

    # Loop through the list and print each number
    for number in list_of_int:
        print(number, end=" ")

    # Print a blank line to keep output clean
    print()

    # Loop through each number in the list
    for number in list_of_int:
        # Add the current number to total
        total += number

    # Calculate the average
    average = total / MAX_ARRAY_SIZE

    # Display the final average
    print("Average:", average)


# Call the main function to start the program
if __name__ == "__main__":
    main()
