def radix(str_number :str, radix: int):
    sum=0
    for e in str_number:
        if e.isnumeric():
            sum += radix*e
        if e.isalpha():
            sum += (ord(e) - 55)
        print(sum)
    return sum
print((ord('F') - 55))
#exit()
r=radix("AF", 16)
print(r)