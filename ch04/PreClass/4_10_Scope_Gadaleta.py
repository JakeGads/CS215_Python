x = 7
def access_global():
    print("X from global", x)

access_global()

def try_mod_gloabal():
    x = 3.5
    print("X from mod", x)

try_mod_gloabal()
print(x)

def mod_x():
    global x
    x = "hello"
    print(x)

mod_x()
print(x)

sum = 10 + 5
print(sum)

sum([10,5])

type(sum)

