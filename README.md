# HCL-TESTING
# hcl-test
# Python programming

# PROGRAM 1
```
nums = input().split(',')
for n in nums:
    if int(n, 2) % 5 == 0:
        print(n)
```


# PROGRAM 2
```
s = input()
letters = 0
digits = 0
for ch in s:
    if ch.isalpha():
        letters += 1
    elif ch.isdigit():
        digits += 1
print("LETTERS", letters)
print("DIGITS", digits)
```


# PROGRAM 3
```
def fact(n):
    if n == 0 or n == 1:
      return 1
    return n * fact(n - 1)

n = int(input())
print(fact(n))
```
