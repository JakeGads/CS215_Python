def varMem():
    # how to find some memory
    variable = 5

    memory = id(variable)

    # for the sake of my sanity this is called mem
    print(id(variable))

    def memTranslator(var):
    
        print(id(var), id(var) == memory) # True

        var = 9

        print(id(var), id(var) == memory) # False 

    memTranslator(variable)

    print(id (variable), id(variable) == memory) # True

    variable = 7

    print(id(variable), id(variable) == memory) # False

def listMem():
    variable = []

    memory = id(variable) # mem

    def memTranslator(var):
        print(id(var), id(var) == memory) # mem

        var = []

        print(id(var), id(var) == memory) # not mem
    
    memTranslator(variable)

    print(id(variable), id(variable) == memory)
    variable.append(5)
    print(id(variable), id(variable) == memory)
    variable = []
    print(id(variable), id(variable) == memory)

def tupleMem():
    variable = (4,3)

    memory = id(variable) # mem

    def memTranslator(var):
        print(id(var), id(var) == memory) # mem

        var = (5,5)

        print(id(var), id(var) == memory) # not mem
    
    memTranslator(variable)

    print(id(variable), id(variable) == memory)
    # variable[0] = 2
    print(id(variable), id(variable) == memory)
    variable = (1,2)
    print(id(variable), id(variable) == memory)



varMem()
# listMem()
# tupleMem()