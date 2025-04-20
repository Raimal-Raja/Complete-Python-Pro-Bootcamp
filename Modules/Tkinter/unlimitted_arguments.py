# if you want to pass more argument than it required
# then use *args args => arguments
# its a positional argument, positions matters
def add(*args):
    print(args)
    sum = 0
    for n in args:
        sum += n
    return sum

# add(21,3,5,5,6)
print(add(21,3,5,5,6))