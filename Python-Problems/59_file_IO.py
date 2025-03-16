# Read Only
# file = open("cipher.txt")
# content = file.read()
# print(content)
#
# file.close()
#
# with open("cipher.txt") as file:
#     content = file.read()
#     print(content)


# Open with writing mode
# with open("cipher.txt",mode="w") as file:
#     file.write(" Hello Professor")
# with open("cipher.txt") as file:
#     content = file.read()
#     print(content)

# Open with adding text mode
with open("cipher.txt",mode="a") as file:
    file.write(" Hello Professor")
with open("cipher.txt") as file:
    content = file.read()
    print(content)