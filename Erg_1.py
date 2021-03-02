# Ergasies_Telous
#Οι εργασίες για το πρώτο εξάμηνο!
import random
import math


def shuffler(x):
    global sq
    i = 0
    while i < x:
        random.shuffle(sq[i])
        i += 1
    random.shuffle (sq)       
    
def hor(x):
    global count
    global sq
    i = 0  
    while i < x:
        j = c = 0
        while j < x:
            if sq[i][j] == 1:
                c += 1
                if c >= 4:
                    count += 1
            else:
                c = 0
                
            j += 1
    
        i += 1    
   
def ver(x):
    global count
    global sq
    i = 0
    while i < x:
        j = c = 0
        while j < x:
            if sq[j][i] == 1:
                c += 1
                if c >= 4:
                    count += 1
            else:
                c = 0
                
            j += 1
        i += 1         
   
def diag(x):
    global count
    global sq
    i = j = c = 0
    while i < x:
        if sq[i][j] == 1:
            c += 1
            if c >= 4:
                count += 1
        else:
            c = 0
            
        i += 1
        j += 1
        
    k = c = c2 = 0
    while k < x - 4:
        i = 0
        while i < x - k - 1:
            j = i + k + 1
            if sq[i][j] == 1:
                c += 1
                if c >= 4:
                    count += 1
            else:
                c = 0
            
            if sq[j][i] == 1:
                if sq[i][j] == 1:
                    c2 += 1
                    if c2 >= 4:
                        count += 1
                else:
                    c2 = 0
                    
            i += 1
        
        k += 1
        
    k = c = c2 = 0
    while k < x - 4:
        i = 0
        while i < x - k - 1:
            j = 5 - i - k - 1
            if sq[i][j] == 1:
                c += 1
                if c >= 4:
                    count += 1
            else:
                c = 0
            
            if sq[i+k+1][j+k+1] == 1:
                if sq[i][j] == 1:
                    c2 += 1
                    if c2 >= 4:
                        count += 1
                else:
                    c2 = 0
                    
            i += 1
        
        k += 1
    
    i = c = 0
    while i < x:
        if sq[i][x-1-i] == 1:
            c += 1
            if c >= 4:
                count += 1
            
        else:
            c = 0
            
        i += 1    
            
print("What size do you want your square 2D list to be? It has to be over 3!")
y = input("Size :")
x = int(y)
while x<4:
    print("The number should be greater than 3!")
    y = input("Size :")
    x = int(y)

sq = []
a = []
y = math.ceil(x/2)
for i in range (x) : 
    for j in range (y):
        a.append(1)
        
    for j in range (y,x):
        a.append(0)
        
    sq.append(a)
    a = []

    
count = 0
i = 0
print("The number of nodes of the list is : \n")
print(x*x)   
while i < 100:
    shuffler(x)
    hor (x)
    ver (x)
    diag (x)
    i += 1
    
aver = count / 100
print("The average number of quadruple ones is:\n")
print(aver)    
