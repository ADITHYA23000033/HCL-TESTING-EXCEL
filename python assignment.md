# Python Assignments
# Author: Adithya V
# Date: 29/09/2026


# 1. Print All Prime Numbers Between Input Range
~~~

start = int(input("Enter starting number: "))
end = int(input("Enter ending number: "))

print("Prime numbers:")

for num in range(start, end + 1):
    if num > 1:
        for i in range(2, int(num ** 0.5) + 1):
            if num % i == 0:
                break
        else:
            print(num, end=" ")

print()
~~~



# 2. Factorial Using Recursion
~~~
def factorial(n):
    if n == 0 or n == 1:
        return 1
    return n * factorial(n - 1)


num = int(input("\nEnter a number for factorial: "))
print("Factorial:", factorial(num))
~~~

# 3. Square of Numbers Using Lambda
~~~

numbers = [1, 2, 3, 4, 5]

square = lambda x: x * x

squares = list(map(square, numbers))

print("\nNumbers:", numbers)
print("Squares:", squares)
~~~


# 4. Find the Second Largest Element in a List
~~~
numbers = [10, 25, 7, 45, 32, 18]

unique_numbers = list(set(numbers))
unique_numbers.sort()

second_largest = unique_numbers[-2]

print("\nList:", numbers)
print("Second largest element:", second_largest)
~~~

# 5. Count Frequency of Characters in a String
~~~

text = input("\nEnter a string: ")

frequency = {}

for char in text:
    if char in frequency:
        frequency[char] += 1
    else:
        frequency[char] = 1

print("Character frequency:")

for char, count in frequency.items():
    print(char, ":", count)
~~~



# 6. Calculate Area of a Circle Using Math Library
~~~
import math

radius = float(input("\nEnter radius of the circle: "))

area = math.pi * radius * radius

print("Area of the circle:", area)
~~~
# 7. Reverse a String Without Using Built-in Reverse
~~~


text = input("\nEnter a string to reverse: ")

reversed_text = ""

for char in text:
    reversed_text = char + reversed_text

print("Original string:", text)
print("Reversed string:", reversed_text)
~~~



# 8. Remove Duplicates from a List
~~~

numbers = [10, 20, 10, 30, 20, 40, 30, 50]

unique_numbers = []

for num in numbers:
    if num not in unique_numbers:
        unique_numbers.append(num)

print("\nOriginal list:", numbers)
print("List after removing duplicates:", unique_numbers)
~~~


# 9. Merge Two Dictionaries
~~~

dict1 = {
    "name": "Adithya",
    "age": 21
}

dict2 = {
    "department": "CSE",
    "college": "Engineering College"
}

merged_dict = {**dict1, **dict2}

print("\nFirst dictionary:", dict1)
print("Second dictionary:", dict2)
print("Merged dictionary:", merged_dict)

~~~

# 10. Fibonacci Series Using Recursion
~~~

def fibonacci(n):
    if n <= 1:
        return n
    return fibonacci(n - 1) + fibonacci(n - 2)


terms = int(input("\nEnter number of Fibonacci terms: "))

print("Fibonacci series:")

for i in range(terms):
    print(fibonacci(i), end=" ")

print()
~~~
