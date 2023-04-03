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
