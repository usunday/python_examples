
def long_repeat(line):
    """
        length the longest substring that consists of the same char
    """
    small_letter = map(chr, range(ord('a'), ord('z')+1))
    big_letter = map(chr, range(ord('A'), ord('Z')+1))
    count=0
    letter=' '
    for ch in small_letter:
        tmp = line.count(ch)
        if(count < tmp):
            count=tmp
            letter=ch

    for ch in big_letter:
        tmp = line.count(ch)
        if(count < tmp):
            count=tmp
            letter=ch
            
    # your code here
    return count
