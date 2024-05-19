from art import logo

alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']

def encrypt(text, shift, direction):
    end_text = ""
    
    if direction == "decode":
            shift *= -1
            
    for latter in text:
        if latter in alphabet:
            position = alphabet.index(latter)
            new_position = position + shift
            end_text += alphabet[new_position]
        else:
            end_text += latter
        
    print(f"The {direction} text is {end_text}")



print(logo)

should_continue = True
while should_continue:
    direction = input("Type 'encode' to encrypt, type 'decode' to decrypt:\n")
    text = input("Type your message:\n").lower()
    shift = int(input("Type the shift number:\n"))
    shift = shift % 26

    encrypt(text, shift, direction)
    
    result = input("Type 'yes' if you want to run again. Otherwise type 'no'. \n")
    if result == 'no':
        should_continue = False
        print("Goodbye")