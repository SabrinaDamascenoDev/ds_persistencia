with open("arquivo3.txt", "r", encoding="latin1") as file:
    doc = file.read()
print(doc)

with open("arquivo1.txt", "r", encoding="utf-8") as file:
    doc = file.read()
print(doc)

with open("arquivo2.txt", "r", encoding="utf-16") as file:
    doc = file.read()
print(doc)