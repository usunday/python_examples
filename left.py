
def left_join(phrases):
    """
        Join strings and replace "right" to "left"
    """

    string = ','.join(phrases).replace('right', 'left')
    return string

s=left_join(("left", "right", "left", "stop"))
print(s)