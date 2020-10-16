def two_fer(name = 'Default'):
    if (type(name) == int):
        raise Exception("There is a number!")
    elif name == 'Default':
        return("One for you, one for me.")
    else: 
        return("One for " + name + ", one for me.")
    
