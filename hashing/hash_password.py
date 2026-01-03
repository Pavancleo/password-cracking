import hashlib
import os

password = input("Enter password: ")

# Generate random salt
salt = os.urandom(16)

# Create hash using SHA-256
hash_object = hashlib.sha256(salt + password.encode())
hashed_password = hash_object.hexdigest()

print("\n--- Password Hashing ---")
print("Salt (hex):", salt.hex())
print("Hashed Password:", hashed_password)