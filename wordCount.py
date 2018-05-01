import re
from collections import Counter

def popular_words(text, words):
    # your code here
    text=re.sub("[,]","",text)
    c=Counter(text.lower().split())

    return{word:c[word] for word in words}

d=popular_words('''
When I was One,
I had just begun.
When I was Two,
I was nearly new.
''',['i', 'was', 'three'])

print(d)