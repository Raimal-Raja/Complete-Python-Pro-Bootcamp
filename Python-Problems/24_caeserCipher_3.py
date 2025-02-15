# alphabet_list = [chr(i) for i in range(ord('a'), ord('z') + 1)]
alphabet_list = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z',]
Direction = input("Type 'encode' to encrypt and 'decode' to decrypt: ")
text = input("type your message: ").lower()
shift = int(input("Type the shift number: "))

def encrypt(plain_text, shift_amount):
    cipher_text = ""
    for letter in plain_text:
        position = alphabet_list.index(letter)
        new_position = position + shift_amount
        new_letter = alphabet_list[new_position]
        cipher_text += new_letter
    print(f'The encoded text is {cipher_text}')
    
def decrypt(plain_text, shift_amount):
    cipher_text = ""
    for letter in plain_text:
        position = alphabet_list.index(letter)
        new_position = position - shift_amount
        new_letter = alphabet_list[new_position]
        cipher_text += new_letter
    print(f'The decrypt text is {cipher_text}')
 
if Direction == 'decode':    
    decrypt(plain_text=text, shift_amount= shift)
elif Direction == 'encode':
    encrypt(plain_text= text, shift_amount= shift)
else:
    print('Please enter valid command!')