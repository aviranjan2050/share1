file= open("demon.txt", 'r')
print(file.read())
file.close()

file1 = open("demon.txt", 'a')
file1.write("\ni am good")
#file1.writelines("how ae you")
file1.close()