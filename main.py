import os

def main_menu():
    """Display the main menu and get the user's choice."""
    print("\n\033[96m--- Welcome to the Code Encryptor/Decryptor! ---\033[0m")
    print("\033[92m1. Encrypt Python Code\033[0m")
    print("\033[92m2. Decrypt Python Code\033[0m")
    print("\033[92m3. Exit\033[0m")
    choice = input("\033[94mPlease enter your choice (1/2/3): \033[0m")
    return choice

if __name__ == "__main__":
    while True:
        choice = main_menu()
        
        if choice == '1':
            os.system('python encrypt.py')  # Call encrypt.py
        elif choice == '2':
            os.system('python decrypt.py')  # Call decrypt.py
        elif choice == '3':
            print("\033[92mExiting the program. Goodbye!\033[0m")  # Green text
            break
        else:
            print("\033[91mInvalid choice. Please try again.\033[0m")  # Red text