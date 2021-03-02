import random
import math


def shuffler(x):
    global rec
    i = 0
    while i < x:
        random.shuffle(rec[i])
        i += 1
    random.shuffle (rec)       
   
def hor(x,y):
    global count
    global rec
    i = 0  
    while i < x:
        j = 0
        while j<y-2:
            if rec[i][j] == "S" and rec[i][j+1] == "O" and  rec[i][j+2] == "S": 
                j += 2
                count += 1
            else:
                j += 1
                
        i += 1    
    
def ver(x,y):
    global count
    global rec
    j = 0
    while j<y:
        i = 0
        while i<x-2:
            if rec[i][j] == "S" and rec[i+1][j] == "O" and  rec[i][j] == "S":
                i += 2
                count += 1
            else:
                i += 1
                           
        j += 1         
           
def diag(x,y):
    global count
    global rec
    i = 0
    while i<x-2:
        j = 0
        while j<y-2:
            if rec[i][j] == "S" and rec[i+1][j+1] == "O" and  rec[i+2][j+2] == "S":
                count += 1
            
            j += 1
                           
        i += 1         
    
    while i<x-2:
        j = y-1
        while j > 1:
            if rec[i][j] == "S" and rec[i+1][j-1] == "O" and  rec[i+2][j-2] == "S":
                count += 1
            
            j += 1
                           
        i += 1     
        
print("Give the dimensions of the rectangular you want to make.\nNeither height nor width can be less than or equal to 2 simultaneously for the process to work. ")
y = input("Height : ")
h = int(y)
y = input("Width : ")
w = int(y)
while (h<=2 and w<=2):
    print("Neither height nor width can be less than or equal to 2 simultaneously! ")
    y = input("Height : ")
    h = int(y)
    y = input("Width : ")
    w = int(y)

rec = []
a = []
y = math.ceil(w/2)
for i in range (h) : 
    for j in range (y):
        a.append("S")
        
    for j in range (y,w):
        a.append("O")
        
    rec.append(a)
    a = []

    
count = 0
i = 0 
print("The number of nodes of the list is : \n")
print(h*w)   
while i < 100:
    shuffler(h)
    hor (h,w)
    ver (h,w)
    diag (h,w)
    i += 1

aver = count / 100
print("The average number of SOS sequences in the rectangular is:\n")
print(aver)    