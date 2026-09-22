#!/usr/bin/env python3
import sys

if len(sys.argv) != 2:
    print("none")
else:
    param1 = sys.argv[1]
    param2 = input() 
    # if param1 == param2:
    #     print("Good job!")
    # else:
    #     print("Nope, sorry...")
print("param1:", param1)
print("param2:", param2)