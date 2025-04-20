# def createDict(**kwargs):
#     # print(type(kwargs))
#     # print(kwargs)
#
# #     standard way to  loop through dictionay
#     for key, val in kwargs.items():
#         print(f"{key} {val}")
# createDict(name='Raimal Raja', roll=49)
#
#
from django.db.models.fields import return_None


def calculate(n,**kwargs):
    # print(type(kwargs))
    # print(kwargs)

#     standard way to  loop through dictionay
    for key, val in kwargs.items():
        n += kwargs["add"]
        n *= kwargs["multi"]
    return n
print(calculate(3,add=4, multi=2))