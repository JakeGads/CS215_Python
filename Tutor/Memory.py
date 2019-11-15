def varMem():
    # how to find some memory
    variable = "memory"

    memory = id(variable)

    # for the sake of my sanity this is called mem
    print(id(variable)) # mem

    def memTranslator(var):
        print(id(var), id(var) == memory) # mem

        var = "editied memory"

        print(id(var), id(var) == memory) # not mem

    memTranslator(variable)

    print(id (variable), id(variable) == memory) # mem

    variable = "new memory"

    print(id(variable), id(variable) == memory)

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



# varMem()
# listMem()
# tupleMem()