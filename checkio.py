def checkio(data):

    #replace this for solution
    result=False
    
    if(len(data)<10):
        return False
    else:
        result=True
    
    if(re.search("[a-z]+",data)):
        result=True
    else:
        return False
    if(re.search("[A-Z]+",data)):
        result=True
    else:
        return False
    if(re.search("[0-9]+",data)):
        result=True
    else:
        return False
        
    return result 
