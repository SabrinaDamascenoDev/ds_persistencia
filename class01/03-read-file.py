with open("../arquivo.txt", "r") as file:
    #Can break the memory, but if use readline don break
    #To work with larger files, we divide in streams to work separated
    doc = file.read()

print(doc)