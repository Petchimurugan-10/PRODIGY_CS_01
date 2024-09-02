def caesar_cipher(text, shift, mode='encrypt'):
    result = ""
    
    if mode == 'd':
        shift = -shift

    for char in text:
        if char.isupper():
            result += chr((ord(char) + shift - 65) % 26 + 65)
        elif char.islower():
            result += chr((ord(char) + shift - 97) % 26 + 97)
        else:
            result += char

    return result

def main():
    mode = input("Would you like to 'encrypt' or 'decrypt' the message? ('e' or 'd')").strip().lower()
    text = input("Enter your message: ")
    shift = int(input("Enter the shift value (key): "))

    result = caesar_cipher(text, shift, mode)

    print(f"The resulting text is: {result}")

if __name__ == "__main__":
    main()
