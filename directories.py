from pathlib import Path

#all directory access

path = Path() #current directory
for file in path.glob('*.py'):
    print(file)



