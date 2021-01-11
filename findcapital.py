import re

def find_message(text):
    """Find a secret message"""

    a="".join(re.findall('[A-Z]', text))
    print(a)
    return ""

find_message("How are you? Eh, ok. Low or Lower? Ohhh.")