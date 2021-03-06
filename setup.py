#!/usr/bin/env python
from __future__ import print_function

import configure

xdress_logos = ["""                                         
XXXXXXX       XXXXXXXDDDDDDDDDDDDD        
X:::::X       X:::::XD::::::::::::DDD     
X:::::X       X:::::XD:::::::::::::::DD   
X::::::X     X::::::XDDD:::::DDDDD:::::D  
XXX:::::X   X:::::XXX  D:::::D    D:::::D 
   X:::::X X:::::X     D:::::D     D:::::D
    X:::::X:::::X      D:::::D     D:::::D
     X:::::::::X       D:::::D     D:::::D
     X:::::::::X       D:::::D     D:::::D
    X:::::X:::::X      D:::::D     D:::::D
   X:::::X X:::::X     D:::::D     D:::::D
XXX:::::X   X:::::XXX  D:::::D    D:::::D 
X::::::X     X::::::XDDD:::::DDDDD:::::D  
X:::::X       X:::::XD:::::::::::::::DD   
X:::::X       X:::::XD::::::::::::DDD     
XXXXXXX       XXXXXXXDDDDDDDDDDDDD        
""",
]


def main_body():
    print(xdress_logos[0])
    configure.setup()


def main():
    success = False
    try:
        main_body()
        success = True
    finally:
        configure.final_message(success)

if __name__ == "__main__":
    main()
