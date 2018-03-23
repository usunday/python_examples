import math
import re
game_result=["O..",
             "XOX",
             "..O"]

#print(game_result)

result="".join(game_result)

#print(result)

order=math.sqrt(len(result))
#print(order)

Xs=""
Os=""

for i in range(int(order)):Xs+="X"
for i in range(int(order)):Os+="O"

#print(Xs)
#print(Os)
#print(re.findall('(XXX|OOO)+', sample))
rex="("+Xs+"|"+Os+")+"
p=re.compile(rex)

sample=""
for i in range(int(order)):
    for j in range(int(order)):
        sample+=result[i+int(order*j)]
    if(p.findall(sample)):print("found")
    sample=""

sample=""

for i in range(int(order)):
    for j in range(int(order)):
        sample+=result[j+int(order*i)]
    if(p.findall(sample)):print("found")
    sample=""

sample=""   

for i in range(int(order)):
    if (i > 0): sample+=result[int(i*order+i)]
    else : sample+=result[i]
print(sample)    
if(p.findall(sample)):print("found")
sample=""

for i in range(1,int(order)+1):
    if(i==1):
        sample+=result[int(order-1)]
    else:
        sample+=result[int(i*order-i)]
        #print("adr:%d"%int(i*order-i))
    
if(p.findall(sample)):print("found")
