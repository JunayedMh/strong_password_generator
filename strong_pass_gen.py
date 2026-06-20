import random
import string

def generate_password(length=12):
    characters = string.ascii_letters + string.digits + string.punctuation
    password = ''.join(random.choice(characters) for _ in range(length))
    return password

length = int(input("Enter password length (default 12): ") or 12)
password = generate_password(length)
print(f"Generated password: {password}")