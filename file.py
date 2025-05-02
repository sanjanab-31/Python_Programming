# import os

fp=open('file22.txt','w')
fp.write("Hello World\n")
fp.write("Welcome to Python\n")
fp.close()

fp=open('file22.txt','a')
fp.write("This is a new line\n")
fp.close()

fp=open('file22.txt','r+')
fp.write("Lets start")
fp.close()

fp=open('file22.txt','a+')
fp.write("This is end\n")
fp.close()

fp=open('file22.txt','r')
print(fp.read())
fp.close()

fp=open('file22.txt','w+')
fp.write("This is start\n")
fp.close()