# # from dataclasses import dataclass


# f = open("G:/pycharm/test.txt", 'w')
# f.write("THIS IS WRITING SECTION")
# f.write("This is the write command")
# f.write("It allows us to write in a particular file")
# f.write("THIS IS WRITING SECTION")
# f.write("This is the write command")
# f.write("It allows us to write in a particular file")
# f.write("THIS IS WRITING SECTION")
# f.write("This is the write command")
# f.write("It allows us to write in a particular file")
# f.write("THIS IS WRITING SECTION")
# f.write("This is the write command")
# f.write("It allows us to write in a particular file")
# f.write("THIS IS WRITING SECTION")
# f.write("This is the write command")
# f.write("It allows us to write in a particular file")
# # file = open('geek.txt', 'a')
# # file.write("This will add this line")
# # f = open("G:/pycharm/test.txt", 'r')
# # print(f.read())

# with open("G:/pycharm/test.txt", "r")as f:
#     data = f.readlines()
#     print(data)
#     for line in data:
#         # word = line.split()
#         # print(word)
#         print(line)


file1 = open("G:/pycharm/myfile.txt", "w")
L = ["This is Delhi \n", "This is Paris \n", "This is London"]
file1.writelines(L)
file1.close()

# Append-adds at last
file1 = open("G:/pycharm/myfile.txt", "a")  # append mode
file1.write("\nToday \n")
file1.close()

file1 = open("G:/pycharm/myfile.txt", "r")
print("Output of Readlines after appending")
print(file1.read())
print()
file1.close()

# Write-Overwrites
file1 = open("G:/pycharm/myfile.txt", "w")  # write mode
file1.write("Tomorrow \n")
file1.close()

file1 = open("G:/pycharm/myfile.txt", "r")
print("Output of Readlines after writing")
print(file1.read())
print()
file1.close()
