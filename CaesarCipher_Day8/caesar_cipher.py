import art
print(art.logo)
alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']

# Using one function for both encryption and decryption
def caesar(user_text, shift_amount, cipher_direction):
    print(shift_amount)
    result_code = ''
    for character in user_text:
        if character not in alphabet:
            result_code += character
            continue
        index = alphabet.index(character)
        if cipher_direction == 'encode':
            new_index = index + shift_amount
            if new_index > len(alphabet) - 1:
                new_index %= len(alphabet)
            
        elif cipher_direction == 'decode':
            new_index = index - shift_amount
            if new_index < 0:
                new_index %= len(alphabet)
           
        result_code += alphabet[new_index]

    print(f"Your {cipher_direction}d text is {result_code}.")


restart = 'yes'
while restart == 'yes':
    direction = input("Type 'encode' to encrypt, type 'decode' to decrypt:\n").lower()
    if direction != "encode" and direction != "decode":
        print('We can only encode and decode the message for you! Follow the above instructions')
        continue
    text = input("Type your message:\n").lower()
    shift = int(input("Type the shift number:\n"))

    caesar(user_text= text, shift_amount=shift, cipher_direction=direction)
    restart = input("Type yes if you want to go again. Otherwise type no: ").lower()
    
print('Goodbye!🖐 😉. Thank you for using our services this fine day!')