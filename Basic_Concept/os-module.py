import os

print(os.getcwd()) # /media/abid/Lab/Python/codes/Beginner
# print(os.chdir('/home/abid'))

# os.mkdir('demo')
# os.makedirs('demo1/demo2')

# os.rmdir('demo')
# os.removedirs('demo1/demo2')

# os.rename('text.txt', 'demo.txt')
# os.stat('demo.txt')                   info about that file

print(os.environ.get('HOME'))

file_path = os.path.join(os.environ.get('HOME'), 'test.txt')
print(file_path)

print(os.path.dirname('/tmp/text.txt'))
print(os.path.basename('/tmp/text.txt'))
print(os.path.exists('tmp/test.txt'))
# os.path.isdir
# os.path.isfile
print(os.path.splitext('/tmp/test.txt'))

