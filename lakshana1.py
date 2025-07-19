import re
input_file='input.txt'
output_file='email.txt'
with open(input_file,'r') as file:
    text=file.read()
email_pattern=r'[a-zA-Z0-9.-%+-]+@[a-zA-Z0-9,-]+\.[a-zA-Z]{2,}'
emails=re.findall(email_pattern,text)
with open (output_file,'w') as file:
    for email in emails:
        file.write(email+'\n')
print(f"{len(emails)} email(s) extracted and saved to {output_file}.")
