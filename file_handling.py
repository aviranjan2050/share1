#file = open("demo.txt","w")
#file.close()
file = open("demo.txt",'r')
content = file.read() #read all of it
#content = file.read(5) #reads 5 byte of data
#reading first line
#content = file.readline()
print(content)
file.close()