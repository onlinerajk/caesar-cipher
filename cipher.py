# add your code here
def caesar_cipher(text, shift=5):
    encrypted_text = ""
    
    for char in text:
        if char.isupper():
            encrypted_text += chr((ord(char) - 65 + shift) % 26 + 65)
        elif char.islower():
            encrypted_text += chr((ord(char) - 97 + shift) % 26 + 97)
        else:
            encrypted_text += char
            
    return encrypted_text

# Ask the user for input
plain_text = input("Enter the text to encrypt: ")

# Encrypt and print the result
encrypted_text = caesar_cipher(plain_text)
print("Encrypted text:", encrypted_text)

