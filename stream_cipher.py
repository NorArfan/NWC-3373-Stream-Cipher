def encrypt(plaintext, key):
    ciphertext = []

    for i in range(len(plaintext)):
        p = ord(plaintext[i])
        k = ord(key[i % len(key)])
        ciphertext.append(p ^ k)

    return ciphertext


def decrypt(ciphertext, key):
    plaintext = ""

    for i in range(len(ciphertext)):
        k = ord(key[i % len(key)])
        plaintext += chr(ciphertext[i] ^ k)

    return plaintext


plaintext = "Cryptography"
key = "KEY"

ciphertext = encrypt(plaintext, key)
print("Ciphertext:", ciphertext)

decrypted = decrypt(ciphertext, key)
print("Decrypted:", decrypted)