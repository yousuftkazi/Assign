import hashlib
import os

def hash_file(filename):

   h = hashlib.sha1()
   
   with open(filename,'rb') as file:
       chunk = 0
       while chunk != b'':
           chunk = file.read(1024)
           h.update(chunk)
  
   return h.hexdigest()




lst=os.listdir("test/")
message=[]
for i in lst:
    message.append( hash_file("test/"+i))
    print(os.path.abspath(i))
message.sort()
#print(message)