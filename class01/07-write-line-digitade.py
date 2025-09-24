import sys

with open("../arquivo2.txt", "w") as file:
    for linha in sys.stdin:
        file.write("oi")