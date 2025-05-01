import json

# 4 operations in json

dataDic = {'facebook':{"username":"raimal_professor",'password':"professor"},
           "google":{"username":'rajaraimal','password':"root"}}

# load() => read file and update file update()
with open("password.json",'r') as data_file:
    data = json.load(data_file)
#     print(data)
    data.update(dataDic)


# dump() > write file
# with open("password.json",'w') as data_file:
#     json.dump(dataDic,data_file,indent=4)
