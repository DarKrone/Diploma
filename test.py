import random
import string
slug = ''.join([random.choice(string.ascii_lowercase + string.digits) for n in range(10)])
password = ''.join([random.choice(string.ascii_lowercase + string.digits) for n in range(10)])
print(slug)
print(password)