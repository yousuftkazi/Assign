import os
rootDir=r"C:\Users\yousuf.tanvir\Desktop\Assign"
for dirName, subdirList, fileList in os.walk("."):
    print("found directory: ",dirName)
    for i in fileList:
        print(i)
