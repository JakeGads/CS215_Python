"""
5.7 (DUPLICATE ELIMINATION) Create a function that receives a list and returns a (possibly shorter) 
list containing only the unique values in sorted order. 
Test your function with a list of numbers and a list of strings.
"""

def remove(duplicate): 
    final_list = [] 
    for num in duplicate: 
        if num not in final_list: 
            final_list += [num] 
    return final_list 

def remove2(duplicate):
    return set(duplicate)

def remove3(duplicate):
    duplicate.sort()

    i = 0
    while True:
        if duplicate[i] == duplicate[i+ 1]:
            del duplicate[i]
            i-=1
        i+=1

        if i == len(duplicate) - 1:
            return duplicate



    
if __name__ == "__main__":
    print(remove3([1,1,1,1,1]))
    print(remove3(["Jake", "Ryan", "Jake", "Ryan", "Micker", "Micker", "Ryan", "Ryan", "Ryan", "Ryan", "Ryan", "Brian", "Thomas", "Maggie", "Chris", "Mark", "Paul"]))

