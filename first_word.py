import re
def first_word(text : str) -> str:

    return re.search('[a-zA-Z0-9\']+',text).group()
