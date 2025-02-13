alphabet_list = [chr(i) for i in range(ord('a'), ord('z') + 1)]
Direction = input("Type 'encode' to encrypt and 'decode' to decrypt: ")
text = input("type your message: ").lower()
shift = int(input("Type the shift number: "))
