# alphabet_list = [chr(i) for i in range(ord('a'), ord('z') + 1)]
alphabet_list = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z',]
Direction = input("Type 'encode' to encrypt and 'decode' to decrypt: ")
text = input("type your message: ").lower()
shift = int(input("Type the shift number: "))

def caeser(start_text, shift_amount, cipher_direction):
    end_text = ''
    for letter in start_text:
        position = alphabet_list.index(letter)
        if cipher_direction == 'decode':
            shift_amount *= -1
        new_position = position + shift_amount
        end_text += alphabet_list[new_position]
    print(f"text {end_text}")
caeser(start_text= text, shift_amount= shift, cipher_direction= Direction)