import base64
import os

def decrypt_code(encrypted_code):
    """Decrypt the given base64 encoded string."""
    decrypted_bytes = base64.b64decode(encrypted_code)
    return decrypted_bytes.decode('utf-8')

def read_encrypted_file(file_path):
    """Read the encrypted code from a file."""
    try:
        with open(file_path, 'r') as file:
            encrypted_code = file.read().strip()
            return encrypted_code
    except FileNotFoundError:
        print(f"Error: The file '{file_path}' was not found.")
        return None

def main():
    print("--- Decrypt Python Code ---\n")
    
    # Prompt user for input method
    while True:
        method = input("Do you want to (1) enter encrypted code manually or (2) read from a file? (1/2): ")
        if method == '1':
            print("Enter the encrypted code (type 'END' on a new line to finish):")
            encrypted_lines = []
            while True:
                line = input()
                if line.strip() == "END":
                    break
                encrypted_lines.append(line)
            encrypted_code = "\n".join(encrypted_lines)
            break
        elif method == '2':
            file_path = input("Enter the path of the file containing the encrypted code: ")
            encrypted_code = read_encrypted_file(file_path)
            if encrypted_code is not None:
                break
        else:
            print("Invalid option. Please enter '1' or '2'.")
    
    # Attempt to decrypt the code
    print("\nDecrypting code...")
    try:
        decrypted_code = decrypt_code(encrypted_code)
        print("\nDecrypted code:\n")
        print(decrypted_code)
    except Exception as e:
        print(f"Error during decryption: {e}")
    else:
        print("\n--- Done ---")

if __name__ == "__main__":
    main()