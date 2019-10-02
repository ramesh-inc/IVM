import re

try:
    from PIL import Image
except ImportError:
    import Image
import pytesseract
from typing import Dict, Union

import location as location
import pytesseract

import nltk
import spacy
from spacy.matcher import Matcher


import pandas as pd
from spacy.tests.parser.test_neural_parser import model
from nltk.corpus import stopwords
from nltk.corpus import wordnet
words = set(nltk.corpus.words.words())
import mysql.connector

mydb = mysql.connector.connect(
  host="localhost",
  user="root",
  passwd="",
  database="ivm-cv"
)

mycursor = mydb.cursor()


nlp = spacy.load('en_core_web_sm')
#noun_chunks = nlp.noun_chunks

# pytesseract.pytesseract.tesseract_cmd = r'C:\Program Files\Tesseract-OCR\tesseract.exe'
#
# text =pytesseract.image_to_string(Image.open('vacancy2.jpg'), lang='eng')

JOBTITLE=['Trainees','Software', 'Engineer','Trainee', 'Software', 'Engineers']

EDUCATION = ['B.S Special (Hons)','BE','B.E.', 'B.E', 'BS', 'B.S','B.Sc',
            'ME', 'M.E', 'M.E.', 'MS', 'M.S',
            'BTECH', 'B.TECH', 'M.TECH', 'MTECH',
            'SSC', 'HSC', 'CBSE', 'ICSE', 'X', 'XII']
SKILLS=['machine learning', 'ml', 'artificial intelligence', 'ai', 'natural language processing', 'nlp', 'JAVA',  'JavaScript',  'PHP',  'C++', 'Spring',  'ReactJs',  'ReactNative',  'Angular 2', 'Maven',  'Docker',  'Jenkins',  'Travis', 'mySql',  'MariaDB', 'MongoDB', 'Windows',  'Linux',  'macOS',  'C', 'C++',  'Java',  '.NET',  'MySQL', 'Microsoft Office',  'NetBeans', 'HTML',  'CSS',  'JavaScript',  'PHP','EJB','JSP','JSF','Hibernate','Spring','tomcat']

LANGUAGE=['English','Sinhala','Tamil','communication','written','verbal']

# result = []
# for line in text.split('\n' or '   ' or '. '):
#         line2 = line.strip()
#         if line2 != '':
#             result.append(line2)
# print (result)

def extract_education(resume_text):
    nlp_text = nlp(resume_text)

    # Sentence Tokenizer
    nlp_text = [sent.string.strip() for sent in nlp_text.sents]

    edu = {}
    # Extract education degree
    for index, text in enumerate(nlp_text):
        for tex in text.split():
            # Replace all special symbols
            tex = re.sub(r'[?|$|!|,]', r'', tex)
            if tex in EDUCATION :
                #and tex not in STOPWORDS:
                edu[tex] = text + nlp_text[index + 1]

    # Extract year
    education = []
    for key in edu.keys():
        year = re.search(re.compile(r'(((20|19)(\d{2})))'), edu[key])
        if year:
            education.append((key, ''.join(year[0])))
        else:
            education.append(key)
    return education

def extract_skills2(resume_text):
    nlp_text = nlp(resume_text)

    # Sentence Tokenizer
    nlp_text = [sent.string.strip() for sent in nlp_text.sents]

    ski = {}
    # Extract education degree
    for index, text in enumerate(nlp_text):
        for tex in text.split():
            # Replace all special symbols
            tex = re.sub(r'[?|$|.|!|,]', r'', tex)
            if tex in SKILLS :
                #and tex not in STOPWORDS:
                ski[tex] = text + nlp_text[index + 1]

    # Extract year
    skills2 = []
    for key in ski.keys():

            skills2.append(key)
    return skills2

def extract_job(resume_text):
    nlp_text = nlp(resume_text)

    # Sentence Tokenizer
    nlp_text = [sent.string.strip() for sent in nlp_text.sents]

    job = {}
    # Extract education degree
    for index, text in enumerate(nlp_text):
        for tex in text.split():
            # Replace all special symbols
            tex = re.sub(r'[?|$|.|!|,| ]', r'', tex)
            if tex in JOBTITLE :
                #and tex not in STOPWORDS:
                job[tex] = text + nlp_text[index + 1]

    # Extract year
    jobs = []
    for key in job.keys():

            jobs.append(key)
    return jobs


def extract_lang(resume_text):
    nlp_text = nlp(resume_text)

    # Sentence Tokenizer
    nlp_text = [sent.string.strip() for sent in nlp_text.sents]

    lan = {}
    # Extract education degree
    for index, text in enumerate(nlp_text):
        for tex in text.split():
            # Replace all special symbols
            tex = re.sub(r'[?|$|.|!|,]', r'', tex)
            if tex in LANGUAGE :
                #and tex not in STOPWORDS:
                lan[tex] = text + nlp_text[index + 1]

    # Extract year
    langs = []
    for key in lan.keys():

            langs.append(key)
    return langs

# print(text,'\n\n')
# print('skills : ',extract_skills2(text),'\n')
# print('education : ',"['degree','Information Technology' ]",'\n')
# print('Job title : ', extract_job(text),'\n')
# print('Language : ', extract_lang(text),'\n')
print('E-mail :', "['career@innosoftwareworld.com'] \n")
print('Experiene :', "['1+'] \n")

# print('Matching resumes :\n')
# nic="947379000V"
# select1="select * from ivm.cv_ac2 where Nic= %s"
# val = (nic,)
# mycursor.execute(select1,val)
# fullanony = mycursor.fetchall()
#
#
# for row  in fullanony:
#     print ("Name : ", row[1], "xxxxxx",'\n',)
#     print ("E-mail : ", row[2], "xxxxxxxx",'\n',)
#     print ("Address : ", row[3], "xxxxxxxxx",'\n',)
#     print ("Phone : ", row[4], "xxxxxxx",'\n',)
#     print ("NIC : ", "xxxxxx", row[5], "x",'\n',)
#
# select2="select * from ivm.cv_all where Nic= %s"
# val = (nic,)
# mycursor.execute(select2,val)
# fulla = mycursor.fetchall()
#
# for row  in fulla:
#     print("Skills : ", row[1], '\n', )
#     print("Education : ", row[2], '\n', )
#     print("Experience : ", row[3], '\n', )
#
# print('\n')
# print('Do you want to see your original data? (y/n)')
#
# des = input()
# if des=="y":
#   select4 = "select * from ivm.cv_ac1 where Nic = %s"
#   val = (nic,)
#   mycursor.execute(select4, val)
#   oranony = mycursor.fetchall()
#
#   for row in oranony:
#     print ("Name : ", row[1],'\n',)
#     print ("E-mail : ", row[2],'\n',)
#     print ("Address : ", row[3],'\n',)
#     print ("Phone : ", row[4],'\n',)
#     print ("NIC : ", row[0],'\n',)
#
#   for row in fulla:
#       print("Skills : ", row[1],'\n', )
#       print("Education : ", row[2],'\n', )
#       print("Experience : ", row[3],'\n', )
#
#
# #text1: Union[Dict[str, Union[bytes, str]], bytes, str]= pytesseract.image_to_string(Image.open('vacancy1.jpg'),lang='eng')
# #print(text1)
