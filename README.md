# Password Cracking and Hashing Algorithms

## Objective
To understand how passwords are securely stored using hashing and salting techniques, and to demonstrate why weak and unsalted passwords are vulnerable to dictionary-based cracking attacks.

---

## Project Description
This project explores password security by implementing:
- Password hashing using SHA-256
- Random salting to strengthen password storage
- A controlled dictionary-based password cracking demonstration

The project clearly compares **unsalted hashes** and **salted hashes** to show the importance of secure password storage practices.

---

## Tools & Technologies Used
- Python
- hashlib library (SHA-256)
- Custom wordlist for controlled testing

---

## Project Structure

password-security-project/
├── hashing/
│ ├── hash_password.py # Salted hashing
│ └── hash_unsalted.py # Unsalted hashing
├── cracking/
│ └── crack_hash.py # Dictionary-based cracker
├── wordlist.txt
└── README.md

## How To Use This Project

### Prerequisites
- Python 3.x installed on your system
- Basic knowledge of terminal/command prompt

---

### Step 1: Generate an Unsalted Hash (For Cracking Demo)

1. Navigate to the hashing folder:
 cd hashing

2. Run the unsalted hashing script:
 python hash_unsalted.py

3. Enter a weak password (e.g., password)

4. Copy the generated hash

### Step 2: Crack the Unsalted Hash

1. Navigate to the cracking folder:
 cd ../cracking

2. Run the cracking script:
 python crack_hash.py

3. Paste the copied hash when prompted

### Step 3: Generate a Salted Hash

1. Navigate back to the hashing folder:
 cd ../hashing

2. Run the salted hashing script:
 python hash_password.py

3. Enter the same password used earlier 

4. Copy the generated salted hash

### Step 4: Attempt to Crack the Salted Hash

1. Navigate to the cracking folder again:
 cd ../cracking

2. Run the cracking script:
 python crack_hash.py

3. Paste the salted hash
 
### Key Observations

 * Unsalted hashes are insecure against dictionary attacks

 * Salting significantly increases password security

 * Salting prevents the use of precomputed rainbow tables

 * Strong password storage is critical for real-world applications

### Disclaimer

This project is strictly for educational purposes only.
All demonstrations are performed on self-created passwords in a controlled environment.
No real user data or systems were harmed or targeted.




