import re

def long_repeat(line) :

    small_letter = map(chr, range(ord('a'), ord('z')+1))
    big_letter = map(chr, range(ord('A'), ord('Z')+1))

    count=0
    for ch in small_letter:
        itr=re.finditer(ch+'+',line)
        if(itr!=None):
            for tok in itr:
                tok_len=len(tok.group())
                if(count < tok_len): count=tok_len

    return count
