#!/usr/bin/env python3
import sys
from unittest import case

parameters = sys.argv[1:]

match parameters:
    case []:
        print("none")
        
    case _:
        for arg in parameters:
            if arg.endswith("ism"):
                continue
            else:
                print(f"{arg}ism")
