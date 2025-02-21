len("Hello")


# Type () function helps us know what data type we are working with. (Type checking)

print(type("Hello")) # This is called type checking.

print(type("Hello")) # <class 'str'>

print(type(123)) # <class 'int'>

print(type(456.789)) # <class 'float'>

print(type(True)) # <class 'bool'>

# Turning one type to another (Type conversion)
# int("123") turns the string "123" into an integer.

print(int("123") + int("456"))

# You cannot turn abc into an int. You have to convert the right data type. You will get ValueError

int()
float()
str()
bool()

# Fix this
#print("Number of letters in your name: " + len(input("Enter your name"))) # Error Received is "TypeError: can only concatenate str (not "int") to str)

# Solution
print("Number of letters in your name: " + str(len(input("Enter your name"))))

