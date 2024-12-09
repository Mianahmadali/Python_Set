"""Create a set of even numbers from 1 to 20 using set comprehension.

Write code to create a set containing even numbers between 1 and 20"""
even_numbers = {num for num in range(1, 21) if num % 2 == 0}
print(even_numbers)
