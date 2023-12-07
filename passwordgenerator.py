import random

def generate_password(length=8, complexity=1):
  """
  Generates a random password of the specified length and complexity.

  Args:
    length: The desired length of the password.
    complexity: The complexity of the password (1 for basic, 2 for medium, 3 for high).

  Returns:
    A random password.
  """
  char_sets = {
    1: "abcdefghijklmnopqrstuvwxyz",
    2: "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789",
    3: "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789!@#$%^&*()_+-={}[]|\\:;'<,>.?/"
  }

  char_set = char_sets.get(complexity, char_sets[1])

  password = ''.join(random.sample(char_set, length))
  return password

print("Welcome to the Password Generator!")
password_length = int(input("Enter desired password length: "))
password_complexity = int(input("Enter desired password complexity (1 for basic, 2 for medium, 3 for high): "))

password = generate_password(password_length, password_complexity)
print(f"Generated password: {password}")