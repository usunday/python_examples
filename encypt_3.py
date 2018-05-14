def to_encrypt(text, delta):
    #replace this for solution
    k=ord('z')-ord('a')+1
    rst=""
    for e in text:
        if e.isalpha():
            if (ord(e) + delta) < ord('a'):
                rst += chr(ord(e) + k + delta)
            elif (ord(e) + delta) > ord('z'):
                rst += chr(ord(e) - k + delta)
            else :
                rst += (chr(ord(e) + delta))
        else:
            rst += e

    return rst

rst=to_encrypt("important text", 10)
print(rst)