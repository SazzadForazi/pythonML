import os
f= open("pythonbasic\\demo.txt","a")
f.write("hello there")
f.write("Now the file has more content!")
f.close()
f=open("pythonbasic\\demo.txt","r")
print(f.read())

# os.rmdir("pythonbasic\\demo.txt")
