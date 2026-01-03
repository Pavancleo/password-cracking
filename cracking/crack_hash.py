import hashlib

target_hash = input("Enter hash to crack: ")

with open("wordlist.txt", "r") as file:
    for word in file:
        word = word.strip()
        hashed_word = hashlib.sha256(word.encode()).hexdigest()

        if hashed_word == target_hash:
            print("✅ Password Found:", word)
            break
    else:
        print("❌ Password Not Found in Wordlist")
