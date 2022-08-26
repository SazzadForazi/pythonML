import os

path = os.chdir(
    "D:\\face_project\\zzzzzzzzzzz\\final_sorting\\with_mask\\external19")
i = 4453
for file in os.listdir(path):
    new_file_name = "external19_{}.jpg".format(i)
    os.rename(file, new_file_name)
    i = i+1
