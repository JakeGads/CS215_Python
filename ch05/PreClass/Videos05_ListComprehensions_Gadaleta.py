# Jake Gadaleta
#5_11 - 5_13
list1 = []
for item in range(6):
    list1.append(item)
list1
list2 = [item for item in range(6)]
list2
list3 = [item ** 3 for item in range(6)]
list3
list4 = [item for item in range(11) if item % 2 == 0]
list4
colors = ['red', 'orange','yellow','green','blue']
colors2 = [item.upper() for item in colors]
colors2
colors
numbers = [10,3,7,1,9,4,2,8,5,6]
for value in (x ** 2 for x in numbers if x % 2 != 0):
    print(value, end=' ')
def is_odd(x):
    return x % 2 != 0
list(filter(is_odd, numbers))
[item for item in numbers if is_odd(item)]
list(filter(lambda x: x% 2 != 0, numbers))
list(map(lambda x: x ** 2, numbers))
[item ** 2 for item in numbers]
list(map(lambda x : x ** 2, filter(lambda x : x % 2 != 0, numbers)))
