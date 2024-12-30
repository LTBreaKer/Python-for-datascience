#!/home/aharrass/Python_For_Data_Science/Starting/venv/bin/python


import sys

if len(sys.argv) > 2:
    print("AssertionError: more than one argument is provided")
    sys.exit()
if len(sys.argv) < 2:
    print("AssertionError: no argument is provided")
    sys.exit()

try:
    arg = int(sys.argv[1])
except Exception:
    print("AssertionError: argument is not an integer")
    sys.exit()

print("I'm Even") if not arg % 2 else print("I'm Odd")
