name = "John"
age = 23
mylist = [2, 3, 4, 5]

print("Hello, %s!" % name)
print("%s is %d years old." % (name, age))
print("A list: %s" % mylist)

# string operation

str = "Hello world ! I am learning python."
print("single quotes are ' '")
print(len(str))
print(str.index("o"))
print(str.count("l"))
print(str[3:7])         #[start, stop]
print(str[1:7:2])       #[start, stop, step]
print(str[: : -1])      #reverse a string 
print(str.upper())
print(str.lower())
print(str.startswith("Hello"))
print(str.endswith("kkdkdff"))
print(str.split(" "))
