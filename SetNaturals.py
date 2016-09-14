def natural_as_set(n):
    '''(int) -> str
    REQ: n > 0
    Returns a string containing the set-theoretic definition of the natural
    number n'''
    # This definition is recursive. We start as defining 0 as {} (the empty
    # set,
    if (n == 0):
        result = "{}"
    # and any n > 0 as the set of all natural numbers beween 0 and n,
    # i.e. n = {0, 1, 2, ..., n-1}
    # This makes expressing it as a string easy, since we can recursively swap
    # those numbers for their own set representations and build up that way
    else:
        result = "{"
        for i in range(n):
            result += natural_as_set(i) + ", "
        # The result will have an extra comma and space at the end
        result = result[:-2] + "}"
    return result
