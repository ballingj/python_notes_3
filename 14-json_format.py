import json

# Extract data into Python
with open('listings.json', 'r') as infile:
    contents = json.load(infile)  # Parse JSON data into a Python object. (A)

print(contents)
print(type(contents))
print(type(contents[0]))

# Filter out all unavailable job listings.
available = [job for job in contents if job["available"]]

# Write available listings to an output file.
with open('available-listings.json', 'w') as outfile:
    json.dump(available, outfile, indent=2)

# out to string instead of file
out_string = json.dumps(available)
print(out_string)

# in from string instead of from a file
in_string = json.loads(out_string)
print(in_string[0]['description'])
