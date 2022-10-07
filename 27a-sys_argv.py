"""
1. Import the sys library and replace the name variable with the
   appropriate argv index.
2. Add a second argument representing the city and extend the print
   to include this argument.
3. Try running python3 cli.py sam 'new york' and make sure you're 
   getting the output: hello, sam from new york. Notice the single
   quotes in the CLI argument to prevent new and york from being passed
   as two different arguments.

"""

import sys

name = sys.argv[1]
city = sys.argv[2]

print(f'hello, {name} from {city}')
