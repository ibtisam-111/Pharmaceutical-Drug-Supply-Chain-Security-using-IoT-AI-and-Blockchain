from Crypto.Cipher import AES
import base64

def encrypt_data(data, key):
    cipher = AES.new(key, AES.MODE_EAX)
    nonce = cipher.nonce
    ciphertext, tag = cipher.encrypt_and_digest(data.encode('utf-8'))
    return base64.b64encode(nonce + ciphertext).decode('utf-8')

def decrypt_data(ciphertext, key):
    data = base64.b64decode(ciphertext)
    nonce = data[:16]
    ciphertext = data[16:]
    cipher = AES.new(key, AES.MODE_EAX, nonce=nonce)
    return cipher.decrypt(ciphertext).decode('utf-8')

# Example usage
key = b'Sixteen byte key'
encrypted = encrypt_data('Sensitive Data', key)
print('Encrypted:', encrypted)
decrypted = decrypt_data(encrypted, key)
print('Decrypted:', decrypted)
