import base64
import os

def encrypt_code(code: str) -> str:
    """Encrypt the given Python code using base64 encoding."""
    encoded_bytes = base64.b64encode(code.encode('utf-8'))
    encoded_str = encoded_bytes.decode('utf-8')
    return encoded_str

def save_encrypted_code(filename: str, encrypted_code: str):
    """Save the encrypted code to a file."""
    with open(filename, 'w') as file:
        file.write(encrypted_code)
    print(f"\033[92mEncrypted code saved to '{filename}'\033[0m")  # Green text

def get_code_from_user():
    """Get code from the user or read from a file."""
    choice = input("\033[94mDo you want to (1) enter code manually or (2) read from a file? (1/2): \033[0m")
    if choice == '1':
        print("\033[93mEnter the Python code to encrypt (type 'END' on a new line to finish):\033[0m")
        lines = []
        while True:
            line = input()
            if line.strip().upper() == 'END':
                break
            lines.append(line)
        return "\n".join(lines)  # Join all lines into a single string
    elif choice == '2':
        filename = input("\033[93mEnter the filename to read code from: \033[0m")
        if os.path.isfile(filename):
            with open(filename, 'r') as file:
                return file.read()
        else:
            print("\033[91mFile not found. Exiting.\033[0m")  # Red text
            exit(1)
    else:
        print("\033[91mInvalid choice. Exiting.\033[0m")  # Red text
        exit(1)

if __name__ == "__main__":
    print("\n\033[96m--- Encrypt Python Code ---\033[0m\n")
    
    # Get code to encrypt
    code_to_encrypt = get_code_from_user()
    
    # Check if code is empty
    if not code_to_encrypt.strip():
        print("\033[91mNo code provided. Exiting.\033[0m")  # Red text
        exit(1)

    # Encrypt the code
    print("\033[93mEncrypting code...\033[0m")  # Yellow text
    encrypted_code = encrypt_code(code_to_encrypt)
    
    # Specify output filename
    output_filename = input("\033[93mEnter the filename to save the encrypted code (default: encrypted_code.txt): \033[0m")
    if not output_filename:
        output_filename = 'encrypted_code.txt'
    
    # Save the encrypted code to a file
    save_encrypted_code(output_filename, encrypted_code)
    
    # Optionally print the encrypted code
    print("\n\033[96mEncrypted code:\033[0m")
    print(encrypted_code)
    print("\n\033[92m--- Done ---\033[0m\n")