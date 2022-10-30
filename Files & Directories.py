from pathlib import Path

path = Path("Learning1")
print(path.exists()) #check if this directory exist

path = Path("Emails")
print(path.mkdir())

path = Path("Emails.py")
print(path.rmdir())

