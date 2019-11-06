def deleteDuplicates(numbers):
    """This functionall duplicatesfrom numbers and returnsAsorted list of the unqiue values"""
    numbersCopy = sorted(numbers)

    for num in numbers:
        if(numbersCopy.count(num) > 1):
            occurrences =  numbersCopy.count(num)
            first = numbersCopy.index(num)
            del numbersCopy[first+1:first+occurrences]
    
    return numbersCopy


def is_ordered(*l):
    # cleaning the data
    cleaned_list = []
    for i in l[0]:
        cleaned_list.append(i)
    return cleaned_list == sorted(cleaned_list)



if __name__ == "__main__":        
    l = [5, 3, 2, 1, 1, 1, 4, 5, 4, 6, 2, 2, 2]
    print(deleteDuplicates(l))
    print(is_ordered(l))
    tupy = 1,2,3,4,5,6,100
    print(is_ordered(tupy))

