import os

p = "G:/pycharm/newfolder/pp"

# try:
#     os.mkdir(p)
#     print("folder has been created")
# except FileExistsError:
#       print("file already exists.")


if not os.path.exists(p):

    os.makedirs(p)

else:
    print("Folder Already Exists")
