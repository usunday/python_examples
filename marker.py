import re
def between_markers(text: str, begin: str, end: str) -> str:
    """
        returns substring between two given markers
    """
    # your code here
    pos_begin = text.find(begin)
    pos_end = text.find(end)

    if pos_end < 0 : pos_end=len(text)+1

    if pos_begin < 0 :
        pos_begin = 0
    else : pos_begin += len(begin)


    print(pos_begin, pos_end)
    print(text[pos_begin:pos_end])
    return text[pos_begin:pos_end]
    exit()
    begin=re.search(begin, text).end()
    end = re.search(end, text).start()

    print(begin,end)
    if end==0 : end=len(text)
    if begin > end : begin=0
    print(text[begin:end])
    return text[begin:end]

between_markers("No [b]hi","[b]","[/b]")