# You are asked to ensure that the first and last names of people begin with a capital letter in their passports.
# For example, alison heck should be capitalised correctly as Alison Heck.
# Given a full name, your task is to capitalize the name appropriately.
# Input Format
# A single line of input containing the full name,
# Constraints
#     The string consists of alphanumeric characters and spaces.
# Note: in a word only the first character is capitalized. Example 12abc when capitalized remains 12abc.
# Output Format
# Print the capitalized string,

# Sample Input:
# chris alan
# Sample Output:
# Chris Alan

#!/bin/python3

# Complete the solve function below.
def solve(s):
    list_words = s.split(" ")
    new_string = ''
    for word in list_words:
        #print(word.capitalize())
        new_string = new_string + " " + word.capitalize()
    return new_string[1:]


def solve_easy(s):
    print(s.title())

if __name__ == '__main__':
    answer = solve("is this a good string in capital letters?")
    print(answer)

    #solve_easy("is this a good string in capital letters?")