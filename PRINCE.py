import os, platform

try:

    import requests

except:

    os.system('pip install requests')
    os.system('git pull')

import requests

bit = platform.architecture()[0]

if bit == '64bit':

    from public64 import login

    login()

elif bit == '32bit':

    from public import login

    login()
