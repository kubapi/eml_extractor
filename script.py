import email
from email import policy
from email.parser import BytesParser
import glob
import os

path = './mails/'

eml_files = glob.glob(path + '*.eml')
for eml_file in eml_files:
    with open(eml_file, 'rb') as fp: 
        pass
    fp.close()
 