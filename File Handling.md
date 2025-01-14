

#File Handling:
*************
Reading,writing,deleting,creating of File

#modes:
******
r-Read
w-write
a-append
r+-Read write
w+-write Read  

#process:
********
1)open()
2)read/write
3)close()


#read file
**********
file1 = open("D:\Big_Data\DataSets\word1.txt",mode='r')
print(file1.read())
file1.close()

#read firstline for file
************************
firstline = open("D:\Big_Data\DataSets\word.txt",mode='r')
print(firstline.readline())
firstline.close()

#convert lines into list format
*******************************
list = open("D:\Big_Data\DataSets\word.txt",mode='r')
print(list.readlines())
list.close()


#write to file
**************
file1 = open("D:\Big_Data\DataSets\word1.txt",mode='w')
file1.write('Hi sandeep!')
file1.close()


#append to file
***************
file1 = open("D:\Big_Data\DataSets\word1.txt",mode='a')
file1.write('How are you?')
file1.close()

#read+write file
****************
file1 = open("D:\Big_Data\DataSets\word1.txt",mode='r+')
print(file1.read())
file1.write('how about you?')
file1.close()


#write+read file
****************
file1 = open("D:\Big_Data\DataSets\word1.txt",mode='w+')
file1.write('i am a big data engineer')
file1.seek(0)
print(file1.read())
file1.close()



#with read statment:
********************
with open("D:\Big_Data\DataSets\word1.txt",'r') as File:
    File=File.read()
    print(File)


#with write statment:
*********************
with open("D:\Big_Data\DataSets\word1.txt",'w') as File:
    File.write('How are you?')
	 
	
#tell:
******
tells current position of the pointer

file = open("D:\Big_Data\DataSets\word1.txt",mode='r')
print(file.read())
print(file.tell())          #gives cursor location
file.close()

#seek:
******
moves cursor pointer to specified location
file = open("D:\Big_Data\DataSets\word1.txt",mode='r')
print(file.read())
file.seek(0)                   #moves cursor location to first index
print(file.tell())
file.close()



