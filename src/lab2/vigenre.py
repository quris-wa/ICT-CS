"""Шифр Винежера"""


def encrypt_vigenere(plaintext: str, keyword: str) -> str:
    """
    Encrypts plaintext using a Vigenere cipher.
    >>> encrypt_vigenere("PYTHON", "A")
    'PYTHON'
    >>> encrypt_vigenere("python", "a")
    'python'
    >>> encrypt_vigenere("ATTACKATDAWN", "LEMON")
    'LXFOPVEFRNHR'
    """
    ciphertext = ""
    key_length = len(keyword)

    for i in range(len(plaintext)):
        letter = plaintext[i]
        k = keyword[i % key_length]

        if not k.isalpha():
            raise ValueError("Keyword contains special symbol")

        shift = ord(k.upper()) - ord("A")
        if "A" <= letter <= "Z":
            ciphertext += chr((ord(letter) - ord("A") + shift) % 26 + ord("A"))
        elif "a" <= letter <= "z":
            ciphertext += chr((ord(letter) - ord("a") + shift) % 26 + ord("a"))
        else:
            ciphertext += letter

    return ciphertext


def decrypt_vigenere(ciphertext: str, keyword: str) -> str:
    """
    Decrypts a ciphertext using a Vigenere cipher.
    >>> decrypt_vigenere("PYTHON", "A")
    'PYTHON'
    >>> decrypt_vigenere("python", "a")
    'python'
    >>> decrypt_vigenere("LXFOPVEFRNHR", "LEMON")
    'ATTACKATDAWN'
    """
    plaintext = ""
    key_length = len(keyword)

    for i in range(len(ciphertext)):
        letter = ciphertext[i]
        k = keyword[i % key_length]

        if not k.isalpha():
            raise ValueError("Keyword contains special symbol")

        shift = ord(k.upper()) - ord("A")
        if "A" <= letter <= "Z":
            plaintext += chr((ord(letter) - ord("A") - shift) % 26 + ord("A"))
        elif "a" <= letter <= "z":
            plaintext += chr((ord(letter) - ord("a") - shift) % 26 + ord("a"))
        else:
            plaintext += letter

    return plaintext
