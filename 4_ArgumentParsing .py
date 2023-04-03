#Argument Parsing 
import sys
'''
print(sys.argv[0])
print(sys.argv[1])
'''

# Usage: main.py Filename
'''
filename = sys.argv[1]
message = sys.argv[2]

with open(filename,'w+') as f:
    f.write(message)
'''

import getopt

filename="test.txt"
message="Hello"

opts,args=getopt.getopt(sys.argv[1:],"f:m",["filename","message"])

for opt,arg in opts:
    if opt == '-f':
        filename=arg
    if opt== '-m':
        message = arg
        
with open(filename,'w+') as f:
    f.write(message)
    
