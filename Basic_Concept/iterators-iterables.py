# nums = [1, 2, 3]

# for num in nums:
#     print(num)

# i_nums = iter(nums)

# print(i_nums)     # <list_iterator object at 0x7f3bb63ab7b8>
# print(dir(i_nums))

# print(next(i_nums))
# print(next(i_nums))
# print(next(i_nums))

# while True:
#     try:
#         item = next(i_nums)
#         print(item)
#     except StopIteration:
#         break


# *************************************************

class MyRange:

    def __init__(self, start, end):
        self.value = start
        self.end = end

    def __iter__(self):
        return self

    def __next__(self):
        if self.value >= self.end:
            raise StopIteration
        current = self.value
        self.value += 1
        return current



# Generator 
def my_range(start, end):
    current = start
    while current < end:
        yield current
        current += 1

nums = my_range(1, 10)

print(next(nums))
print(next(nums))
print(next(nums))