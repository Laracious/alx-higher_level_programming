#!/usr/bin/python3
import sys

argv = sys.argv[1:]  # exclude the program name from the list of arguments
num_args = len(argv)  # get the number of arguments

# Print the number of arguments and the list of arguments
if num_args == 0:
    print("No argument.", end='\n\n')
elif num_args == 1:
    print("1 argument:", end='\n\n')
else:
    print(f"{num_args} arguments:", end='\n\n')

# Print the position and value of each argument
for i, arg in enumerate(argv, start=1):
    print(f"{i}: {arg}", end='\n')

