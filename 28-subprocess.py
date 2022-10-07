'''
 Subprocess allowa us to interface with software that
 we'd normally execute from a terminal window.
 

import subprocess
import random

p = subprocess.Popen(['emoj', 'dog'], stdout=subprocess.PIPE)
output, err = p.communicate()
p_status = p.wait()

emoji = output.decode('utf-8').split(' ')

emoji = output.decode('utf-8').split(' ')

print(random.choice(emoji))
'''

"""
Popen has been supported since the start of Python3, and
you'll see it used quite often. However, since Python 3.5
a simpler run interface has been introduced (docs). You should
 be aware of (and know how to use) both of these.
"""

import subprocess
import random
p = subprocess.run(['emoj', 'dog'], stdout=subprocess.PIPE)
emoji = p.stdout.decode('utf-8').split(' ')
print(random.choice(emoji))
