def functionC(x):
    print("In Function", x, id(x))

    x *= 10

    print("Changed", x,id(x))

y = 5
print("Prior to Function", y, id(y))

functionC(y)

print("Post function", y,id(y))