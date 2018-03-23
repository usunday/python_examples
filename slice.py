
pawns={"b4", "d4", "f4", "c3", "e3", "g5", "d2"}

count=0
for e in pawns:
    print(e)
    g1=chr(ord(e[0][0])-1)+str(int(e[1])-1)
    g2=chr(ord(e[0][0])+1)+str(int(e[1])-1)
    if (g1 in pawns or g2 in pawns):
        count += 1

print (count)
        
