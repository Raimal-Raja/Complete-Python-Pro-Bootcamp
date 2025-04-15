import pywhatkit as pwk
from pymupdf import message

phone_number = "+923488722984"

message = "hello"

pwk.sendwhatmsg(phone_number, message)
