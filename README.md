# PyCryptic

**PyCryptic** is a Python-based encryption and decryption tool designed to obfuscate and secure Python files or any other file types. The program allows users to encrypt source code or files into base64 format, and later decrypt them back to their original form. The tool works seamlessly with Python scripts and can be extended to handle any file type.

## Features

- **Encrypt Python or any other file type**: The tool can encrypt Python scripts or binary files (e.g., images, text files, etc.).
- **Decrypt the encrypted files**: Decrypts base64-encoded files back to their original format.
- **Error handling and debugging**: Graceful handling of errors with informative messages.
- **Interactive interface**: A user-friendly interface that allows you to choose between encryption or decryption when running the program.
- **Seamless execution**: Decrypts and runs Python code directly from memory without leaving traces of the decrypted file on disk.

## How It Works

The program works in two stages:
1. **Encryption**:
   - Reads a Python file (or any other file) and converts it into a base64-encoded string.
   - Saves the encoded string to an output file.
2. **Decryption**:
   - Reads the base64-encoded string from an encrypted file.
   - Decodes the string back into the original file content.
   - If it's a Python script, the decrypted content can be executed directly from memory.

## Files in the Repository

- **encrypt.py**: This script allows you to encrypt any file (Python or otherwise) into a base64-encoded format.
- **decrypt.py**: This script decrypts the base64-encoded file back to its original form.
- **main.py**: A script that combines encryption and decryption functionality into one program. The user can choose whether to encrypt or decrypt a file through a simple interface.

## Usage Instructions

### 1. Clone the Repository

```bash
git clone [https://github.com/isaac-hobson/PyCryptic] 
cd pycryptic
```

### 2. Encryption

To encrypt a Python file or any other file:

```bash
python3 encrypt.py
```

- You will be prompted to enter the path to the file you want to encrypt.
- After processing, the encrypted base64-encoded content will be saved in a file of your choice.

### 3. Decryption

To decrypt an encrypted file back to its original format:

```bash
python3 decrypt.py
```

- You will be prompted to enter the path of the encrypted file and an output file name for the decrypted content.

### 4. Combined Encryption/Decryption with `main.py`

You can also use `main.py` to select whether you want to encrypt or decrypt a file through a simple prompt.

```bash
python3 main.py
```

- Follow the on-screen instructions to choose whether you want to encrypt or decrypt a file.

## Example Workflow

1. **Encrypt a Python file**:
    - Run `encrypt.py` and input the Python file you want to encrypt (e.g., `target.py`).
    - It will output an encrypted file, for example, `encrypted_code.txt`.
    
2. **Decrypt the file**:
    - Run `decrypt.py`, select the `encrypted_code.txt` file, and provide an output name (e.g., `target_decrypted.py`).
    - The file will be restored to its original state.

## Requirements

- Python 3.x

This program uses only the basic Python standard libraries (e.g., `base64`), so no additional packages are required.

## License

This project is open-source and available for use under the MIT License.

---

**Created by Isaac**
