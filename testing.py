
list = [2,4,8,20]

list.sort(reverse=True)

sub_index = 0
sum = 0
print(list)
while len(list) > 1:
    a=list.pop()
    b=list.pop()
    sum+=a+b
    print (a,b,sum)

