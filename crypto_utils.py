def caesar(plaintext, key, decode=False):
    import string
    key = -key if decode else key
    alphabet = string.ascii_lowercase
    shifted_alphabet = alphabet[key:] + alphabet[:key]
    table = str.maketrans(alphabet, shifted_alphabet)
    return plaintext.translate(table)



