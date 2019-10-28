c = [-45, 6, 0, 72, 1543]
c
c[0]
c[4]
len(c)
c[-1]
c[-5]
a = 1
b = 2
c[a+b]
c[4] = 17
c
s = "hello"
s[0]
s[0] = "H"
c[100]
c[0] + c[1] + c[2]
a_list = []
for number in range(100):
    a_list += [number]
a_list
letters = []
letters += "Python"
letters
list1 = [10,20,30]
list2 = [40,50]
concat_list = list1 + list2
concat_list
for i in range(len(concat_list)):
    print(f"{i}: {concat_list[i]}")
a = [1,2,3]
b = [1,2,3]
c = [1,2,3,4]
a==b
a==c
a<c
c>=b
# Tuples
student_tuple = ()
student_tuple
len(student_tuple)
student_tuple = 'John', "Green", 3.3
student_tuple
len(student_tuple)
another_student = ("Mary", "Red", 3.3)
another_student
a_singleton_tuple = ('red',)
a_singleton_tuple
time_tuple = (9,16,1)
time_tuple
time_tuple[0] * 3600 + time_tuple[1] * 60 + time_tuple[2]
tuple1 = (10,20,30)
tuple2 = tuple1
tuple2
tuple1 += (40,50)
tuple1
tuple2
numbers = [1,2,3,4,5]
numbers += (6,7)
numbers
student_tuple = ('Amanda', 'Blue', [98,75,67])
student_tuple[2]
student_tuple[2][1] = 85
student_tuple