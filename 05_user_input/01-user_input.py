age=input("please enter a number: ")

name = input("please enter your name: ")

print (f"Hello {name } you are age is {age} years old")


a = int(input("Enter a number: "))
b = int(input("Enter another number: "))

print(f"The sum of {a} and {b} is {a + b}")
print(f"The difference of {a} and {b} is {a - b}")

# single line comment

"""This is a multi-line comment
You can write multiple lines here  
and it will be ignored by the interpreter
"""

# escape characters
print("Hello\nWorld")  # New line
print("Hello\tWorld")  # Tab space
print("Hello\\World")  # Backslash
print("Hello\"World")  # Double quote
print("Hello\'World")  # Single quote


## print 
a=5
print("Hello World" ,"hussien" ,a ,sep="*" ,end= "\n")  # Custom separator