import random
import string

def encrpt(a):
    """
    Encrypt the input string by:
    - Moving the first character to the end
    - Adding 3 random characters at the start and end
    """
    if len(a) > 3:
        n = a[1:] + a[0]  # Move first character to last
    else:
        n = a[::-1]  # Reverse for small strings

    prefix = ''.join(random.choices(string.ascii_lowercase, k=3))  # Random prefix
    suffix = ''.join(random.choices(string.ascii_lowercase, k=3))  # Random suffix
    return prefix + n + suffix  # Append prefix & suffix

def dencrpt(x):
    """
    Decrypt the encrypted string by:
    - Removing the first 3 and last 3 characters (randomly added ones)
    - Moving the last character back to the front
    """
    sstr = x[3:-3]  # Remove the first 3 and last 3 random characters
    print(f"String after slicing: {sstr}")

    if len(sstr) > 3:
        dstr = sstr[-1] + sstr[:-1]  # Move last character to the front
    else:
        dstr = sstr[::-1]  # Reverse back for small strings

    return dstr

# Testing
a = input("Enter a message to encrypt: ")  # e.g., "aman"
x = encrpt(a)
print(f"Encrypted: {x}")

d = dencrpt(x)
print(f"Decrypted: {d}")
