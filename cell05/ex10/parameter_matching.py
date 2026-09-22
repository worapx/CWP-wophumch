import sys

if len(sys.argv) != 2:
    print("none")
else:
    param1 = sys.argv[1]
    param2 = str(input("What was the parameter? ")) 
    if param1 == param2:
        print("Good job!")
    else:
        print("Nope, sorry...")