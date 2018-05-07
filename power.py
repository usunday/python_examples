def index_power(array: list, n: int) -> int:
    """
        Find Nth power of the element with index N.
    """
    if n > len(array)-1:
        return -1

    return pow(array[n],n)


r=index_power([0, 1], 0)
print(r)