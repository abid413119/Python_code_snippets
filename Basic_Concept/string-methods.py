# capitalize()
string1 = "python is AWesome."
capitalized_string = string1.capitalize()


# center()
string2 = "Liza"
centered_string = string2.center(24, '-')
print(centered_string)


# casefold()
string3 = "PYTHON IS AWESOME | der Fluß"
print("Lowercase string: ", string3.casefold())


# count(substring, start, end)
string4 = "Python is awesome, isn't it?"
substring = "i"
count = string4.count(substring, 9, 40)
print(count)


# endswith(suffix, start, end)
text = "programming is easy"
result = text.endswith(('programming', 'python'))
result = text.endswith(('is', 'python', 'easy'))
print(result)


# expandtabs()
str = 'xyz\t12345\tabc'
str = str.expandtabs()
print(str)