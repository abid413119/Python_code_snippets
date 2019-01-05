student = {'name': 'John', 'age': 25, 'courses': ['Math', 'CS']}

student['phone'] = '444-55333'
popped = student.pop('phone')

for key, value in student.items():
    print(key, value)

print(len(student))
print(student['name'])
print(student.get('phone', 'Not Found'))
print(student) 