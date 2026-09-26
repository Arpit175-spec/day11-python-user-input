# #DAY 11 — USER INPUT IN PYTHON

---

## 1. Introduction

In many programs, we need data from the user while the program is running.

Python provides the `input()` function to take input from the keyboard.

User input makes programs **interactive** and dynamic.

---

## 2. Basic Syntax of `input()`

```python
variable_name=input("Message to display")
```

- The text inside quotes is called a **prompt**.
- The value entered by the user is stored in the variable.

### Example

```python
name=input("Enter your name: ")
print(name)
```

---

## 3. Important Concept — Input Always Returns String

By default, Python treats user input as a **string (`str`)**, even if you enter numbers.

```python
age=input("Enter age: ")
print(type(age))
```

Output will be:

```
<class 'str'>
```

---

## 4. Taking Numeric Input (Typecasting)

To use numbers in calculations, we convert input into numeric data types.

### Integer Input

```python
num=int(input("Enter a number: "))
print(num+5)
```

---

### Float Input

```python
price=float(input("Enter price: "))
print(price*2)
```

---

## 5. Multiple Inputs

We can take multiple inputs separately.

```python
a=input("Enter first value: ")
b=input("Enter second value: ")
print(a,b)
```

---

## 6. Common Beginner Mistake

If you don’t convert input to numbers, addition behaves like string joining.

```python
a=input("Enter number: ")
b=input("Enter number: ")
print(a+b)
```

If user enters `2` and `3`, output becomes:

```
23
```

Correct way:

```python
a=input("Enter number: ")
b=input("Enter number: ")
print(int(a)+(b))
```

---

or

```python
a=int(input("Enter number: "))
b=int(input("Enter number: "))
print(a+b)
```

# 📝 SUMMARY NOTES — USER INPUT

## Key Points

1. `input()` is used to take data from the user.
2. Input is always stored as **string** by default.
3. Use **typecasting** (`int()`, `float()`) for numeric calculations.
4. Prompt messages make input user-friendly.
5. Multiple values can be taken using `.split()`.

---

✅ **One-line Definition for Notes:**

> User input in Python allows programs to receive data during execution using the `input()` function, making programs interactive.
> 

# 🧪 QUIZ — REDEFINING CALCULATOR USING USER INPUT

## 🎯 Task

In **Day 9**, we created a calculator using fixed values.

Now redefine the same calculator using the `input()` function so the user can enter numbers.

---

## 📌 Instructions

1. Take two numbers from the user using `input()`.
2. Convert them into integers.
3. Perform the following operations:
- Addition
- Subtraction
- Multiplication
- Division
1. Print all results clearly.

### Comment the code 👍👍👍👍👍
