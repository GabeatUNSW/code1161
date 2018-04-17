
def loops_1a(): 
    """Make 10 stars.

    Using a for loop
    return a list of 10 items, each one a string with exacly one star in it.
    E.g.: ['*', '*', '*', '*', '*', '*', '*', '*', '*', '*']
    """
    resultlist = []

    for i in range (10):
        resultlist.append('*')
    return resultlist

print (loops_1a())
