#the commands with close the file automatic
with open("../arquivo.txt", "r") as file:
    linha = file.readline()
    #Loop for print the line, without repeat code
    while linha:
        print(linha.rstrip())
        linha = file.readline()