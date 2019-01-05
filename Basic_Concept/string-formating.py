person = {'name': 'Abid', 'age': 23}

# sentence = "My name is " + person['name'] + " I am " + str(person['age']) + " years old."

sentence = "My name is {}. I am {} years old".format(person['name'], person['age'])

print(sentence)

tag = 'h1'
text = 'This is a headline'

html = '<{0}>{1}</{0}>'.format(tag, text)
print(html)



class Person():
    
    def __init__(self, name, age):
        self.name = name
        self.age = age

p1 = Person('Jack', '33')

sentence = 'My name is {0.name} and I am {0.age} years old.'.format(p1)
print(sentence)


man = {'name': 'Jenn', 'age': 23}
sentence = 'My name is {name} and I am {age} years old.'.format(**man)

pi = 3.14159265
sentence = 'Pi is equal to {:.3f}'.format(pi)
print(sentence)

sentence = "1MB is equal to {:,} bytes".format(1000**2)
print(sentence)



import datetime

my_date = datetime.datetime(2018, 12, 24, 12, 30, 45)

