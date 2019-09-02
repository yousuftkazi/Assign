import os
import hashlib
import time

rnd=0
changepath=''
flag=False
keyslist=[]
loc=0

class Node:
    def __init__(self,x,thepath,h):
        
        self.data=x
        self.left=None
        self.right=None
        self.fullhash=None
        self.path=thepath
        self.lefthash=None
        self.righthash=None
        self.hashed=h

class BST:
    def __init__(self):
        self.root=None

    def insert(self,h,path):
        global rnd
        global flag
        global loc
        global keyslist

        if(flag==False):
            #print("HERE")
            rnd = os.urandom(8)
            keyslist.append(rnd)

        self.root=self.insert_helper(self.root,keyslist[loc],path,h)
        loc+=1

    def insert_helper(self,node,x,path,h):
        if(node==None):
            node=Node(x,path,h)
            #print(x)
        elif(x>node.data):
            node.right=self.insert_helper(node.right,x,path,h)
            node.righthash=node.right.fullhash
            
        else:
            node.left=self.insert_helper(node.left,x,path,h)
            node.lefthash=node.left.fullhash

        node.fullhash=node.hashed
        if(node.right!=None):
            node.fullhash+=node.righthash
        if(node.left!=None):
            node.fullhash+=node.lefthash
        return node

    def inOrder(self,node):
        if(node==None):
            return

        self.inOrder(node.left)
        print(node.path)
        self.inOrder(node.right)
        

def findChange(t1,t2):
    global changepath
    if(t1.righthash!=t2.righthash):
        findChange(t1.right,t2.right)
    elif(t1.lefthash!=t2.lefthash):
        findChange(t1.left,t2.left)
    else:
        print(t1.fullhash)
        print(t2.fullhash)
        #print(t1.right)
        #print(len(keyslist))
        changepath=t1.path

    return changepath 


def hash_file(filename):

   h = hashlib.sha1()
   
   with open(filename,'rb') as file:
       chunk = 0
       while chunk != b'':
           chunk = file.read(1024)
           h.update(chunk)
  
   return h.hexdigest()

start_time = time.time()


obj=BST()
#rootDir=r"C:\Users\yousuf.tanvir\Desktop\Assign\test"
#rootDir=r"D:\xampp2\htdocs\magento\app\code"
rootDir=r"D:\xampp2\htdocs\magento\vendor\magento\framework\Api"
for dirName, subdirList, fileList in os.walk(rootDir):
    #print("found directory: ",dirName)
    for i in fileList:
        fullpath=dirName+"\\"+i
        h=hash_file(fullpath)
        #print(h)
        obj.insert(h,fullpath)

#obj.inOrder(obj.root)
print("Started")
flag=True
currentroothash=obj.root.fullhash


print("--- %s seconds ---" % (time.time() - start_time))
#exit()
#print(currentroothash)

while(1):
    inLoop=BST()
    #global rnd
    #rnd=0
    loc=0
    #rootDir=r"C:\Users\yousuf.tanvir\Desktop\Assign\test"
    for dirName, subdirList, fileList in os.walk(rootDir):
    #print("found directory: ",dirName)
        for i in fileList:
            fullpath=dirName+"\\"+i
            h=hash_file(fullpath)
            #print(h)
            inLoop.insert(h,fullpath)



    if(currentroothash!=inLoop.root.fullhash):
        #inLoop.inOrder(inLoop.root)
        print("Change Detected")
        findChange(obj.root,inLoop.root)
        print(changepath)
        #print(inLoop.root.fullhash)
        break
    

    #time.sleep(60)
    






# obj.insert(4)
# obj.insert(10)
# obj.insert(2)
# obj.insert(3)
# obj.insert(11)
#obj.inOrder(obj.root)


