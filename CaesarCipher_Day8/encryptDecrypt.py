import art
print(art.logo)
alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']

direction = input("Type 'encode' to encrypt, type 'decode' to decrypt:\n").lower()

def encrypt(message, shift_amount):
    cipher_text = ''
    for character in message:
        if character not in alphabet:
            result_code += character
            continue
        index = alphabet.index(character)
        new_index = index + shift_amount
        if new_index > len(alphabet) - 1:
            new_index %= len(alphabet)
        cipher_text += alphabet[new_index]
    print(f"Your encoded text is {cipher_text}.")

def decrypt(cipher_text, shift_amount):
    message = ''
    for character in cipher_text:
        if character not in alphabet:
            result_code += character
            continue
        index = alphabet.index(character)
        new_index = index - shift_amount
        # Python can evaluate negative indices, but if shift number is greater than 26
        if new_index < 0:
            new_index %= len(alphabet)
        message += alphabet[new_index]
    print(f"Your decoded text is {message}.")

if direction == 'e' or direction == 'encode':
    text = input("Type your message:\n").lower()
    shift = int(input("Type the shift number:\n"))
 
    encrypt(message=text, shift_amount=shift)
elif direction == 'd' or direction == 'decode':
    text = input("Type your coded message:\n").lower()
    shift = int(input("Type the shift number:\n"))
    
    decrypt(cipher_text=text, shift_amount=shift)
else:
    print('We can only encode and decode the message for you!')