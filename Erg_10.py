import json


def depth_di(dic):
    global max_dep
    if dic != "{}":
        dep = 0
        for x in dic:
            if type(dic[x]) == list:
                dep += 1
                dep += depth_li(dic[x])
                max_dep = max(max_dep, dep)
                
            elif type(dic[x]) == dict:
                print("boy")
                dep += 1
                dep += depth_di(dic[x])
                max_dep = max(max_dep, dep)
          
    else:
        dep = -1
         
    return dep
                
def depth_li(dic):
    global max_dep     
    if dic != "[]":
        dep = 0
        for x in range(len(dic)):
            if type(dic[x]) == list:
                dep += 1
                dep += depth_li(dic[x])
                max_dep = max(max_dep, dep)
                
            elif type(dic[x]) == dict:
                print("boy")
                dep += 1
                dep += depth_di(dic[x])
                max_dep = max(max_dep, dep)
            
    else:
        dep = -1
        
    return dep 

print("Give the file path that leads to the text file you want to check!\nThe name of the file must be included at the end of the path!")
path = input("Path : ")
f = open(path)
x = f.readline()
f.close()
x.strip() 
x.strip("'")
x.replace(":","=")
dic = json.loads(x)
if dic != {}:
    max_dep = 1
    dep = depth_di(dic)
    max_dep = max(max_dep, dep)
else:
    max_dep = 0
    
print("The depth of the dictionary is : ",max_dep)