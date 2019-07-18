#! python3

import pyperclip, re

text = str(pyperclip.paste()) # copy from Clipboard

strongPassword = re.compile(r'''(
    (?=.*\d) 
    (?=.*[a-z])
    (?=.*[A-Z])
    [^\s]{8,}
    )''', re.VERBOSE) 

res = []                            
for potentialPassword in strongPassword.findall(text):
    res.append(potentialPassword)                        
    print(potentialPassword)

if len(res) > 0:
    pyperclip.copy('\n'.join(res))
    print('Copied to clipboard...')
else:
    print('found no potential passwords')

                        
