import math


print("Copy and paste the path of the ASCII text file you want to check!\nOf course the text file should be included with it's name. ")
path = input("Path : ")
f = open(path, "r")
f.read()
end = f.tell()
f.close()
f = open("two_cities_ascii.txt", "r")
numbers = []
counters = {}
i = 65 #Ψάχνουμε τις μονές τιμές των Κεφαλαίων σε ASCII
while i <= 90:
    numbers.append(i)
    counters[i] = 0
    i += 2    
i = 97 #Ψάχνουμε τις μονές τιμές των Πεζών σε ASCII
while i <= 122:
    numbers.append(i)
    counters[i] = 0
    i += 2  
    
i = 0
m = 0
y = f.readline(1)
while i < end:
    i += 1
    if y != "" and y != "\n" and y != "\r":
        m += 1
        if (ord(y)>=65 and ord(y)<=90 or ord(y)>=97 and ord(y)<=122) and ord(y)%2 != 0:
            temp = counters[ord(y)]
            counters[ord(y)] = temp + 1
            
    y = f.readline(1)

f.close()
pie = []
for x in numbers:
    if counters[x] != 0:
        
        y = (counters[x]/m)*100
        n = math.ceil(y)
        c = "*"
        for k in range(n-1):
            c = c + "*"
        
        pie.append(c)
    else:    
        pie.append(" ")

j = 0    
for x in numbers:
    print(chr(x), ": ", pie[j])
    j += 1    