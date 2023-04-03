#Decorators

'''
def mydecorator(function):
    def wrapper():
        print("Im decorating your function!")
        function()
    return wrapper

def hello_world():
  print("Hello world!")
  
mydecorator(hello_world)()
'''

'''
def mydecorator(function):
    def wrapper():
        print("Im decorating your function!")
        function()
    return wrapper
    
@mydecorator
def hello_world():
  print("Hello world!")
  
hello_world()
'''

'''
def mydecorator(function):
    def wrapper(*args,**kwargs):
        print("Im decorating your function!")
        function(*args,**kwargs)
    return wrapper
    
@mydecorator
def hello(Person):
  print(f"Hello {Person}")
  
hello("Mike")
'''

# Practical Example 1 -Logging
'''
def logged(function):
    def wrapper(*args,**kwargs):
        value=function(*args,**kwargs)
        with open('logfile.txt','a+') as f:
            fname=function.__name__
            print(f"{fname} returned value {value}")
            f.write(f"{fname} returned value {value}\n")
        return value
        
    return wrapper
 
@logged       
def add(x,y):
    return x+y
    
print(add(10,20))
'''

# Practical Example 2 -Timing

import time
def timed(function):
    def wrapper(*args,**kwargs):
        before=time.time()
        value=function(*args,**kwargs)
        after=time.time()
        fname=function.__name__
        print(f"{fname} took {after-before} seconds to execute!")
        return value
        
    return wrapper

 
@timed
def myfunction(x):
    result=1
    for i in range(1,x):
        result *= i
        
    return result
    
myfunction(10)
