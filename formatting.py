for i in range(1, 13):
    print("No. {0} squared is {1} and cubed is {2}".format(i, i ** 2, i ** 3))
# ** operator in this instance is the Exponent Operator

print()

# to format the output so it's more readable we add a `:` then
# specify its width
for i in range(1, 13):
    print("No. {0:2} squared is {1:3} and cubed is {2:4}".format(i, i ** 2, i ** 3))

print()

# to Left align we add a `<` sign after the `:`
for i in range(1, 13):
    print("No. {0:2} squared is {1:<3} and cubed is {2:<4}".format(i, i ** 2, i ** 3))
# to Right align we add a `>` sign after the `:`
# to center we add a `^` sign after the `:`
print()

# `f` in our placeholder formatting accesses the `floating point` format

print("Pi is approximately {0:12}".format(22 / 7))
print("Pi is approximately {0:12f}".format(22 / 7))
print("Pi is approximately {0:12.50f}".format(22 / 7))
print("Pi is approximately {0:52.50f}".format(22 / 7))
print("Pi is approximately {0:62.50f}".format(22 / 7))
print("Pi is approximately {0:<72.50f}".format(22 / 7))
print("Pi is approximately {0:<72.54f}".format(22 / 7))


# f-string (which won't work on versions earlier than Python 6)
# only need to add the `f` key before the `"`

greeting = "hello"
age = 26
name = "adamas"

print(type(greeting))
print(type(age))

print(name + f" is {age} years old")
print(type(age))

print(f"Pi is approximately {22 / 7:12.50f}")
pi = 22 / 7
print(f"Pi is approximately {pi:12.50f}")