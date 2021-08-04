print("Hello World")
print("So it turns out python does add a \\n at the end of strings but abstracts it")
print("But we can", end=" ")
print("do this to allow us to have separate print statements", end=" ")
print("on different lines of the ide but it would print out all in one line")

# Python variables are references to objects but the actual data is contained
# in the objects
i = 42  # i is a reference to an int object that holds the data 42
print(i)
i += 1
print(i)
i += 0.11  # now x is a reference to a float object and the int object is orphaned and removed by python
print(i)
i = "forty"  # now x is a reference to a string object and the float object is orphaned and removed by python
print(i)

y = i  # here y is referencing the now string object "forty" that i is also referencing
print("i is ", end="")
print(i)
print("y is ", end=" ")
print(y)
y = 78  # here a new int object is created and y now references this object instead

# Every instance (object or variable) has an identity, i.e., an integer unique within the script
# or program, i.e., other objects have different identities
# we can use the function id() to check the identity of an instance

x = 42
id(x)
y = x
print("X's identity = ", id(x), "   Y's identity = ", id(y))
y = 78
print("X's identity = ", id(x), "   Y's identity = ",  id(y))

# numbers can be of any size. there is no long int in python 3 just int

# there are two types of division, "true division" and "floor division"
# true division is just regular division
# "//" or floor division operator divides and rounds down
print(7 / 3)  # true division
print(7 // 3)  # floor division

s = "Hello"
print(s[0])  # you can access the elements of a string through indexing like in c

print(s[-1])  # you can get the last character in the string like this
print(s[-2])  # you get the second to last character in the string like this and so on and so forth

# there are no character data types in python. a single character is a string of size one

# You can repeat strings with the asterisk operator "Hello" * 3
print("Hello " * 3)

# You can also do substrings. ie. for string "Hello" [2:3]
print("Hello" [2:4])

xy = 9

if xy == "9":
    print("XY is a string " + xy, end=" ")
    print("This is another statement.", end=" ")

print(len("Bishoy"))

