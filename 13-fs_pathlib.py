from pathlib import Path

# Get an instance of a Path subclass describing the interpreter's current location (which is usually, but not necessarily, the directory containing your Python files).
here = Path('.')

print(here)  # => .

absol = here.absolute()

print(absol) # =>  /home/jeff/python_dev/misc_python-note-3

# Resolve symbolic links and `..` segments into an absolute `Path`.
here = here.resolve()

print(here)     # => /home/jeff/python_dev/misc_python-note-3

# Navigate up the chain of parents. A purely lexical operation, so it's important to call `.resolve()` or a similar method first.
parent = here.parent

print(parent)  # => /home/jeff/python_dev

# Navigate to a subfolder or subfile. Hooray for magic methods (`__div__`) and polymorphism!
child = here / 'subfolder' / 'subfile.txt'

print(child)  # => /home/jeff/python_dev/misc_python-note-3/subfolder/subfile.txt
