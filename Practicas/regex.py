#! python3

import re, pyperclip

#create a regex for phone numbers

phoneRegex = re.compile(r'''  
(                                 
((\d\d\d)|(\(\d\d\d))))?  
(\s|-)         
\d\d\d           
-
\d\d\d\d
(((ext(\.)?\s)|x)   
(\d{2,5}))?
)         
''', re.VERBOSE)

#create a regex for email addresses

emailRegex = re.compile('''
[a-zA-Z0-9_.+]+                        
@                        
[a-zA-Z0-9_.+]+                           
''', re.VERBOSE)

#Get the text off the clipboard

text = pyperclip.paste()

#Extract the email/phone from this text
extractedPhone = phoneRegex.findall(text)
extractedEmail = emailRegex.findall(text)

allPhoneNumbers = []
for phoneNumber in extractedPhone:
    allPhoneNumbers.append(phoneNumber[0])
#Copy the extracted email/phone to the clipboard
results = '\n'.join(allPhoneNumbers) + '\n' + '\n'.join(extractedEmail)
pyperclip.copy(results)