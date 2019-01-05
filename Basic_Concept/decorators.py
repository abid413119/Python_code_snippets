# *******************************************************************************
#                             Function decorator                                *
# *******************************************************************************

## clouser
# def outer_function(msg):

#     def inner_function():
#         print(msg)
    
#     return inner_function


# hi_function = outer_function("Hi")
# bye_function = outer_function("Bye")

# hi_function()
# bye_function()


## Decorator example
def decorator_function(original_function):
    def wrapper_function(*args, **kwargs):
        print('Wrapper function executed this before {} function'.format(original_function.__name__))
        return original_function(*args, **kwargs)
    return wrapper_function


# behind the scene [
# def display():
#     print('display function ran')

# display = decorator_function(display)
# display()
# ]

@decorator_function
def display():
    print('display function ran')

@decorator_function
def display_info(name, age):
    print('Info: ({}, {})'.format(name, age))

# display_info('abid', 24)
# display()



# *******************************************************************************
#                             class decorator                                   *
# *******************************************************************************

class DecoratorClass(object):
    def __init__(self, original_function):
        self.original_function = original_function
    
    def __call__(self, *args, **kwargs):
        print('call method executed this before {} function'.format(self.original_function.__name__))
        return self.original_function(*args, **kwargs)


@DecoratorClass
def display_for_dec_class():
    print('display function ran')

@DecoratorClass
def display_info_for_dec_class(name, age):
    print('Info: ({}, {})'.format(name, age))

# display_info_for_dec_class('abid', 24)
# display_for_dec_class()



# *******************************************************************************
#                             practical example of decorator                    *
# *******************************************************************************

# example 1

def my_logger(orig_function):
    import logging
    logging.basicConfig(filename='{}.log'.format(orig_function.__name__), level=logging.INFO)

    def wrapper(*args, **kwargs):
        logging.info(
            'Ran with args: {}, and kwrags: {}'.format(args, kwargs))
        return orig_function(*args, **kwargs)

    return wrapper


@my_logger
def display_info_logger(name, age):
    print('display info ran with arguments({}, {})'.format(name, age))

# display_info_logger('abid', 23)



# example 2

def my_timer(orig_function):
    import time

    def wrapper(*args, **kwargs):
        t1 = time.time()
        result = orig_function(*args, **kwargs)
        t2 = time.time() - t1
        print('{} ran in: {} sec'.format(orig_function.__name__, t2))
        return result
    
    return wrapper

import time

@my_timer
def display_info_timer(name, age):
    time.sleep(1)
    print('display_info ran with arguments({}, {})'.format(name, age))

display_info_timer('abid', 25)