# code that uses regular expressions to extract critical information from files, 
# such as email addresses, phone numbers (7 digit standard), URLs, and ZIPS.

import pyperclip, re

#   PHONE         | EMAIL        | ZIP      | URL
#   --------------|--------------|----------|------------
#   area code*    | username     | 6 digits | protocol
#   separator*    | @            |          | server
#   1st 3 digits  | domain       |          | file name
#   separator     | .<something> |          |
#   last 3 digits |              |          |
#   extension*    |              |          |
#
#   *optional

text = str(pyperclip.paste())

phoneRegex = re.compile(r'''(
    (\d{3}|\(\d{3}\))?
    (\s|-|\.)?
    (\d{3})
    (\s|-|\.)
    (\d{4})
    (\s*(ext|x|ext.)\s*(\d{2,5}))?
    )''', re.VERBOSE)

emailRegex = re.compile(r'''(
    [a-zA-Z0-9._%+-]+
    @
    [a-zA-Z.-_]+
    (\.[a-zA-Z]{2,4})
    )''', re.VERBOSE)

zipRegex = re.compile(r'\d{6}')

urlRegex = re.compile(r'http.*?\.[a-zA-Z]{2,4}')

res = []

for number in phoneRegex.findall(text):
    phoneNum = '-'.join([number[1], number[3], number[5]])
    if number[8] != '':
        phoneNum += ' x' + number[8]
    res.append(phoneNum)

for email in emailRegex.findall(text):
    res.append(email[0])

for url in urlRegex.findall(text):
    res.append(url)

for ZIP in zipRegex.findall(text):
    res.append(ZIP)
    
if len(res) > 0:
    pyperclip.copy('\n'.join(res))
    print('Copied to clipboard...')
else:
    print('phone numbers or email addresses not found')
