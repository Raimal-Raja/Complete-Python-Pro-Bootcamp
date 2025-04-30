try:
   file =  open('myfile.txt',mode='r')
except FileNotFoundError:
    file = open('myfile.txt','w')
else:
    content = file.read()
    print(content)
finally:
    file.close()
    print('file was closed')