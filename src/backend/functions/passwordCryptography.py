from Crypto.Cipher import AES
from Crypto.Util import Counter
from Crypto import Random
from Crypto.Hash import SHA3_512
import binascii
from src.backend.configureSecrets import secret_key
# import base64

# AES supports multiple key sizes: 16 (AES128), 24 (AES192), or 32 (AES256).
key_bytes = 32


def hash_pass(password):
    hashed_object = SHA3_512.new()
    hashed_object.update(password.encode("utf8"))
    return hashed_object.hexdigest()


# Takes as input a 32-byte key and an arbitrary-length plaintext and returns a
# pair (iv, ciphertext). "iv" stands for initialization vector.
def encrypt(key, plaintext):
    assert len(key) == key_bytes

    # Choose a random, 16-byte IV.
    init_vec = Random.new().read(AES.block_size)

    # Convert the IV to a Python integer.
    iv_int = int(binascii.hexlify(init_vec), 16)

    # Create a new Counter object with IV = iv_int.
    ctr = Counter.new(AES.block_size * 8, initial_value=iv_int)

    # Create AES-CTR cipher.
    aes = AES.new(key.encode("utf8"), AES.MODE_CTR, counter=ctr)

    # Encrypt and return IV and ciphertext.
    cipher_text = aes.encrypt(plaintext.encode("utf8"))
    return init_vec, cipher_text


# Takes as input a 32-byte key, a 16-byte IV, and a ciphertext, and outputs the
# corresponding plaintext.
def decrypt(key, init_vec, cipher_text):
    assert len(key) == key_bytes

    # Initialize counter for decryption. iv should be the same as the output of
    # encrypt().
    iv_int = int(binascii.hexlify(init_vec), 16)
    ctr = Counter.new(AES.block_size * 8, initial_value=iv_int)

    # Create AES-CTR cipher.
    aes = AES.new(key.encode("utf8"), AES.MODE_CTR, counter=ctr)

    # Decrypt and return the plaintext.
    plaintext = aes.decrypt(cipher_text)
    return plaintext


# (iv, ciphertext) = encrypt(secret_key, 'hello')
# print(f"iv:{iv}")
# url_safe_iv = base64.b64encode(iv).decode("utf8")
# print(f"formatted iv:{url_safe_iv}")
# print(base64.b64decode(url_safe_iv))
# print(ciphertext)
# print(base64.b64encode(ciphertext).decode("utf8"))
# print(decrypt(secret_key, iv, ciphertext).decode("utf8"))

# print(hash_pass("hello"))
# (iv, ciphertext) = encrypt(secret_key, hash_pass("hello"))
# print(decrypt(secret_key, iv, ciphertext).decode("utf8"))
