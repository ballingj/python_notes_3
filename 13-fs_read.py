# (1) Extract data from the `queries.txt` file into Python.
with open('queries.txt', 'r') as infile:
    # Read one big string - the contents of this file.
    contents = infile.read()
    
print(contents)

# (2) Transform the data within Python.
queries = contents.split('\n')  # Split the string into a list by line breaks.

print(queries)

# Normalize each query with the stripped, lowercased version of every other line.
normalized = [query.strip().lower() for query in queries[::2]]

print(normalized)

# (3) Write the normalized queries out to a file.
with open('normalized-queries.txt', 'w') as outfile:
    for query in normalized:
        # It might be better to use outfile.writelines here, but let's practice `.write`-ing strings.
        outfile.write(query + '\n')

# This is incorrect as each item is overwritten by the one after it 
# for query in normalized:
#     with open('normalized-queries.txt', 'w') as outfile:
#         # It might be better to use outfile.writelines here, but let's practice `.write`-ing strings.
#         outfile.write(query + '\n')
