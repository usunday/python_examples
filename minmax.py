def min(*args, **kwargs):
    key = kwargs.get("key", None)

    return getSortedFirst(args,key,False)


def max(*args, **kwargs):
    key = kwargs.get("key", None)

    return getSortedFirst(args,key,True)

def getSortedFirst(args, key, reverse):
    if len(args) is 1 :
        args=iter(args[0])
                  
    return sorted(args, key=key, reverse=reverse)[0]
