"""
Caesar Cipher - Text Encryption and Decryption
Index Number: 10355283

Each letter is shifted by a fixed number of positions in the alphabet.
Letter case is preserved; digits, spaces and punctuation are left unchanged.
"""


def shift_char(ch: str, shift: int) -> str:
    """Shift a single character by `shift` positions (letters only)."""
    if ch.isascii() and ch.isalpha():
        base = ord("A") if ch.isupper() else ord("a")
        return chr((ord(ch) - base + shift) % 26 + base)
    return ch


def encrypt(text: str, key: int) -> str:
    """Encrypt text by shifting each letter forward by `key`."""
    return "".join(shift_char(c, key) for c in text)


def decrypt(text: str, key: int) -> str:
    """Decrypt text by shifting each letter backward by `key`."""
    return "".join(shift_char(c, -key) for c in text)


def read_key() -> int:
    """Keep asking until the user enters a valid whole-number key."""
    while True:
        try:
            return int(input("Enter shift key (a whole number, e.g. 3): "))
        except ValueError:
            print("Invalid key. Please enter a whole number.")


def main() -> None:
    print("=== Caesar Cipher: Encrypt / Decrypt ===")
    print("Index Number: YOUR_INDEX_NUMBER\n")

    while True:
        print("1. Encrypt a message")
        print("2. Decrypt a message")
        print("3. Quit")
        choice = input("Choose an option (1-3): ").strip()

        if choice == "1":
            text = input("Enter text to encrypt: ")
            key = read_key()
            print(f"Encrypted text: {encrypt(text, key)}\n")
        elif choice == "2":
            text = input("Enter text to decrypt: ")
            key = read_key()
            print(f"Decrypted text: {decrypt(text, key)}\n")
        elif choice == "3":
            print("Goodbye!")
            break
        else:
            print("Invalid choice. Please enter 1, 2 or 3.\n")


if __name__ == "__main__":
    main()
