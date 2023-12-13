# f = open('mydata.txt','r')
# print(f)   ## giving object of data  --> <_io.TextIOWrapper name='mydata.txt' mode='r' encoding='UTF-8'>
# print(f.read())   ## Displays data from file.
# print("*"*50)

# print(f.readline()) # Reads only first line of data.
# print(f.readline())  # reads 2nd line
# print(f.readline(10), end="")  # reads only 10 letters from 3rd line
# print("*"*50)

## For writing in the file
# f1 = open("Ankurdata.txt", "w")   ## W for writing in the file  
# f1.write("Hello, Its Ankur from Neosoft.")   ##Msg to write in the file
# print("*"*50)

# for data in f:     ## To read data line by line
#     print(data)


## To read image
f2 = open("./File Handling/P1654116.JPG",'rb')     ## To read image in binary format
# for data in f2:
#     print(data)         ## printing binary data

f3 = open("./File Handling/Mypic.JPG",'wb')
for data in f2:
    f3.write(data)