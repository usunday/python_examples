def second_index(text: str, symbol: str):
    """
        returns the second index of a symbol in a given text
    """
    # your code here
    result = first = text.find(symbol)+1
    
    if(result == -1) : return None
    
    result = text[first:].find(symbol)
    
    if(result == -1) : return None
    
    return result+first
