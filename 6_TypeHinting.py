#Type Hinting
#pip install mypy or pip3 install mypy

'''
def myfunction(myparameter: int):
    print(myparameter)
    
myfunction("Hello world")
'''

def myfunction(myparameter: int) -> str:
    return f"{myparameter+10}"
    
print(myfunction(10))
