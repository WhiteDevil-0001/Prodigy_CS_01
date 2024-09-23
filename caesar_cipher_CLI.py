def caesar_cipher(text, shift, mode):
    result = ""
    
    # Shift for decryption will be negative of encryption
    if mode == "decrypt":
        shift = -shift
    
    for char in text:
        if char.isalpha():
            # Keep track of uppercase and lowercase
            offset = 65 if char.isupper() else 97
            # Perform the shift
            result += chr((ord(char) - offset + shift) % 26 + offset)
        else:
            # Leave non-alphabet characters as they are
            result += char
            
    return result

def main():
    print("Caesar Cipher Program")
    
    while True:
        mode = input("Would you like to encrypt or decrypt a message? (enter 'encrypt' or 'decrypt'): ").strip().lower()
        if mode not in ['encrypt', 'decrypt']:
            print("Invalid option. Please enter 'encrypt' or 'decrypt'.")
            continue

        text = input("Enter your message: ")
        try:
            shift = int(input("Enter the shift value: "))
        except ValueError:
            print("Invalid shift value. Please enter a valid integer.")
            continue

        result = caesar_cipher(text, shift, mode)
        print(f"\nThe {mode}ed message is: {result}\n")
        
        # Ask if the user wants to run the program again
        again = input("Would you like to run the program again? (yes/no): ").strip().lower()
        if again != "yes":
            print("Goodbye!")
            break

if __name__ == "__main__":
    main()
