# Caesar Cipher - Text Encryption \& Decryption

**Index Number:** 10355283
**Name:** ISAAC OSEI

## About

A simple Python program that encrypts and decrypts text using the **Caesar Cipher**.
Each letter is shifted by a fixed number of positions (the key) in the alphabet.
Upper/lower case is preserved, and spaces, digits and punctuation stay unchanged.

## How it works

* **Encryption:** `E(x) = (x + key) mod 26`
* **Decryption:** `D(x) = (x - key) mod 26`

Example with key = 3: `Hello, World!` becomes `Khoor, Zruog!`

## How to run

Requires Python 3 (no extra packages needed).

```bash
python caesar\_cipher.py
```

Then choose:

1. Encrypt a message
2. Decrypt a message
3. Quit

## Sample session

```
Choose an option (1-3): 1
Enter text to encrypt: Hello, World!
Enter shift key (a whole number, e.g. 3): 3
Encrypted text: Khoor, Zruog!
```

## Files

* `caesar\_cipher.py` - the program
* `README.md` - this file

