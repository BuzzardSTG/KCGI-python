from platform import python_version

print("static value")
variable = python_version()
print(variable)
# f-strings
print(f"Current version of python is {variable}")
print(f'Current version of python is {python_version()}')