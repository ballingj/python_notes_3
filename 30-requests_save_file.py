"""
This code saves requested file to a disk
"""

import requests
import random

image_url = 'https://pocket-syndicated-images.s3.amazonaws.com/631b9bfb8052e.jpg'

r = requests.get(image_url)
tmp = f'./tmp/{random.randint(0,10000000)}.png'

with open(tmp, 'wb') as img:
    img.write(r.content)

# This approach will also work:
# img = open(tmp, 'wb')
# img.write(r.content)
# img.close()

print(tmp)  # saved where?
