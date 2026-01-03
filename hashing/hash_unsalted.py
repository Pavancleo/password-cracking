import hashlib

password = input("Enter password: ")

hashed = hashlib.sha256(password.encode()).hexdigest()

print("Unsalted Hash:", hashed)

