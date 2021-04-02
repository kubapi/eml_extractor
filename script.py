import email
from email import policy
from email.parser import BytesParser
import glob
import os
import re

def get_name(text):
    pattern = r"(?<=Name: )(.*)(?=<b)"
    try:
        name = re.search(pattern, text).group(1)
        return name
    except:
        return ""

def get_email(text):
    pattern = r"(?<=Email: )(.*)(?=\/a>)"
    try:
        match = re.search(pattern, text).group(1)
        second_pattern = r"(?<=>)(.*)(?=<)"
        email = re.search(second_pattern, match).group(1)
        return email
    except:
        return ""

path = './mails/'

eml_files = glob.glob(path + '*.eml')
for eml_file in eml_files:
    with open(eml_file, 'rb') as fp:
        msg = BytesParser(policy=policy.default).parse(fp)
    text = str(msg.get_body(preferencelist=('html')))
    fp.close()

    # printing findings
    print(get_name((text)))
    print(get_email(text))


