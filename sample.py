# Simple Monoalphabetic Substitution Cipher Program

def encrypt_monoalphabetic(plaintext, key):
    """
    Encrypts plaintext using monoalphabetic substitution cipher.
    
    Args:
        plaintext: The message to encrypt
        key: 26-letter substitution key
    
    Returns:
        Encrypted ciphertext
    """
    # Define the normal alphabet
    alphabet = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
    
    # Initialize empty string for encrypted message
    ciphertext = ""
    
    # Process each character in the plaintext
    for char in plaintext:
        if char.isupper():
            # If uppercase letter, replace with corresponding uppercase letter from key
            index = alphabet.index(char)
            ciphertext += key[index].upper()
        
        elif char.islower():
            # If lowercase letter, replace with corresponding lowercase letter from key
            index = alphabet.index(char.upper())
            ciphertext += key[index].lower()
        
        else:
            # If not an alphabetic character, leave it unchanged
            ciphertext += char
    
    return ciphertext


def decrypt_monoalphabetic(ciphertext, key):
    """
    Decrypts ciphertext using monoalphabetic substitution cipher.
    
    Args:
        ciphertext: The encrypted message
        key: 26-letter substitution key
    
    Returns:
        Decrypted plaintext
    """
    # Define the normal alphabet
    alphabet = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
    
    # Initialize empty string for decrypted message
    plaintext = ""
    
    # Process each character in the ciphertext
    for char in ciphertext:
        if char.isupper():
            # Find position in key and get corresponding alphabet letter
            index = key.upper().index(char)
            plaintext += alphabet[index]
        
        elif char.islower():
            # Find position in key and get corresponding alphabet letter (lowercase)
            index = key.upper().index(char.upper())
            plaintext += alphabet[index].lower()
        
        else:
            # If not an alphabetic character, leave it unchanged
            plaintext += char
    
    return plaintext


# Main Program
print("=" * 60)
print("MONOALPHABETIC SUBSTITUTION CIPHER")
print("=" * 60)
print()

# Step 1: Define a fixed 26-letter substitution key
# Each letter A-Z is replaced by the corresponding letter in this key
substitution_key = "QWERTYUIOPASDFGHJKLZXCVBNM"

print("Substitution Key Mapping:")
print("Normal Alphabet: ABCDEFGHIJKLMNOPQRSTUVWXYZ")
print(f"Cipher Alphabet: {substitution_key}")
print()

# Step 2: Read the plaintext input from the user
message = input("Enter a message: ")
print()

# Step 3 & 4: Encrypt the message
encrypted_message = encrypt_monoalphabetic(message, substitution_key)

# Step 5: Print the encrypted ciphertext
print(f"Encrypted message: {encrypted_message}")
print()

# Additional: Decrypt to verify
decrypted_message = decrypt_monoalphabetic(encrypted_message, substitution_key)
print(f"Decrypted message: {decrypted_message}")
print()

print("=" * 60)
print("RESULT:")
print("=" * 60)
print("The monoalphabetic substitution cipher was implemented")
print("successfully, encrypting messages by mapping each letter")
print("of the plaintext to a unique corresponding letter from")
print("the predefined key.")
print("=" * 60)