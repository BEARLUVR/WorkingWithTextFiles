file = open("exampleText.txt", "r") 
#contents = file.read(5)
contents = file.readline()
file.close
print(contents)