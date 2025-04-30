key = {'book':"The Prophet",
       'Jibran':'khalil Jibran'}
try:
    name = key['Khalil']

except KeyError as message:
    print(f"waring! The key {message} doesn't exist")