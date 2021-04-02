import email
from email import policy
from email.parser import BytesParser
import glob
import os
import re
import pandas as pd

def get_name(text):
    pattern = r"(?<=Name: )(.*)(?=<b)"
    try:
        name = re.search(pattern, text).group(1)
        return name
    except:
        return 0

def get_email(text):
    pattern = r"(?<=Email: )(.*)(?=\/a>)"
    try:
        match = re.search(pattern, text).group(1)
        second_pattern = r"(?<=>)(.*)(?=<)"
        email = re.search(second_pattern, match).group(1)
        return email
    except:
        return 0

path = './mails/'

eml_files = glob.glob(path + '*.eml')
data = []
for eml_file in eml_files:
    with open(eml_file, 'rb') as fp:
        msg = BytesParser(policy=policy.default).parse(fp)
    text = str(msg.get_body(preferencelist=('html')))
    fp.close()

    #collecting findings
    name = get_name(text)
    email = get_email(text)
    if name != 0 and email != 0:
        data.append([name, email])

dataframe = pd.DataFrame(data, columns=["Names", "Emails"]).drop_duplicates()
dataframe.to_csv("data.csv", index=False)
