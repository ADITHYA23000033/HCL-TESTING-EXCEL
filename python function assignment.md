# Python Function Assignments

# Author: Adithya V
# date:29-09-2026

# 1. Calculator Function

```

def calculate(a, b, operation):

    if operation == "+":
        return a + b

    elif operation == "-":
        return a - b

    elif operation == "*":
        return a * b

    elif operation == "/":
        if b == 0:
            return "Cannot divide by zero"
        return a / b

    else:
        return "Invalid operation"


a = float(input("Enter first number: "))
b = float(input("Enter second number: "))
operation = input("Enter operation (+, -, *, /): ")

result = calculate(a, b, operation)

print("Result:", result)

```

# 2. Sum Numbers Using *args

```

def sum_numbers(*args):

    total = 0

    for num in args:
        total += num

    return total


result = sum_numbers(10, 20, 30, 40, 50)

print("Sum:", result)

```

# 3. Employee Information Using **kwargs

```

def employee(**kwargs):

    print("Employee Information")

    for key, value in kwargs.items():
        print(key.capitalize(), ":", value)


employee(
    name="Adithya",
    id="EMP101",
    department="CSE",
    salary=30000
)

```

# 4. Remove Duplicates While Preserving Order

```

def remove_duplicates(lst):

    unique_list = []

    for item in lst:
        if item not in unique_list:
            unique_list.append(item)

    return unique_list


numbers = [10, 20, 10, 30, 20, 40, 30, 50]

result = remove_duplicates(numbers)

print("Original list:", numbers)
print("List without duplicates:", result)

```

# 5. Sort List of Tuples Using Lambda

```

data = [(1, 5), (2, 3), (4, 1)]

sorted_data = sorted(data, key=lambda x: x[1])

print("Original list:", data)
print("Sorted list:", sorted_data)

```
