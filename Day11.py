# input() returns text (str); int() converts the two number inputs before addition.
a=input("Enter a name :")
print("The name is",a)
print("This is a user input program")

x=input("Enter your first no :")
y=input("Enter your second no :")
print("The type of x is",type(x))
print("The type of y is",type(y))
print(int(x) + int(y))