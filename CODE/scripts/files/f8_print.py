import sys


with open(sys.argv[0], "r") as f1:
    with open(sys.argv[0] + "copy", "w") as f2:
        f2.write(f1.read())