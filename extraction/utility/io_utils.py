# import datetime
# import os
# from utility.pdf_utils import pdf_to_text
# from utility.docx_utils import docx_to_text
# from utility.parser_rules import *
# import json
# import time
# import re
#
# invalid_escape = re.compile(r'\\[0-7]{1,3}')
#
# def replace_with_byte(match):
#     return chr(int(match.group(0)[1:], 8))
#
# import mysql.connector
#
# mydb = mysql.connector.connect(
#     host="localhost",
#     user="root",
#     passwd="It16151666@#1",
#     database="ivm"
# )
#
# mycursor = mydb.cursor()
#
#
# def read_pdf_and_docx(file_path, collected=None, command_logging=False, callback=None):
#     if collected is None:
#         collected = dict()
#
#         if os.path.isfile(file_path):
#             txt = None
#
#             if file_path.lower().endswith('.docx'):
#
#                 if command_logging:
#                     print('extracting text from docx: ', file_path)
#                 txt = docx_to_text(file_path)
#                 print(txt)
#                 ivmid = datetime.datetime.now().strftime("%I:%M%p%B%d%Y" + file_path)
#                 email = []
#                 projects = []
#                 degrees = []
#                 university = []
#                 school = []
#                 experience = []
#                 mobile = []
#                 skills = []
#                 for line_index, line in enumerate(txt):
#                     # print('Line #' + str(line_index) + ': ', line)
#
#                     if extract_email(line) is not None:
#                         email.append(line)
#
#                     if extract_sex(line) is not None:
#                         print('Sex :', extract_sex(line))
#
#                     if extract_expertise(line) is not None:
#                         projects.append(line)
#
#                     if extract_degree(line) is not None:
#                         degrees.append(line)
#
#                     if extract_university(line) is not None:
#                         university.append(line)
#
#                     if extract_school(line) is not None:
#                         school.append(line)
#
#                     if extract_experience(line) is not None:
#                         experience.append(line)
#
#                     if extract_mobile(line) is not None:
#                         mobile.append(line)
#
#                 if extract_skills(txt) is not None:
#                     skills.append(extract_skills(txt))
#                 print('Email : ', email)
#                 print('Projects : ', projects)
#                 print('Degree : ', degrees)
#                 print('University : ', university)
#                 print('Scools : ', school)
#                 print('experience : ', experience)
#                 print('Mobile : ', mobile)
#                 print('Skills : ', skills)
#                 experience_yrs = [" "]
#                 objectives = [" "]
#                 ski = json.dumps(skills)
#                 exp = json.dumps(experience)
#                 pro = json.dumps(projects)
#                 expyrs = json.dumps(experience_yrs)
#                 uni = json.dumps(university)
#                 deg = json.dumps(degrees)
#                 obj = json.dumps(objectives)
#
#                 sql0 = "INSERT INTO ivm.cv_q (id,skills,Experience,projects,experience_yrs,university,degree,specialization,objectives) VALUES (%s,%s, %s, %s, %s, %s, %s, %s, %s)"
#                 val = (ivmid, ski, exp, pro, expyrs, uni, deg, deg, obj)
#                 mycursor.execute(sql0, val)
#                 mydb.commit()
#                 x='{"id1":"'+ivmid+'","skills":"'+ski+'","experience":"'+exp+'","projects":"'+pro+'","exy":"'+expyrs+'","uni":"'+uni+'","deg":"'+deg+'","obj":"'+obj+'"} '
#                 y = json.loads(x)
#                 print(y[skills])
#
#
#
#
#             elif file_path.lower().endswith('.pdf'):
#
#                 if command_logging:
#                     print('extracting text from pdf: ', file_path)
#
#                 txt = pdf_to_text(file_path)
#                 print(txt)
#                 ivmid = datetime.datetime.now().strftime("%I:%M%p%B%d%Y" + file_path)
#                 email = []
#                 projects = []
#                 degrees = []
#                 university = []
#                 school = []
#                 experience = []
#                 mobile = []
#                 skills = []
#                 for line_index, line in enumerate(txt):
#                     # print('Line #' + str(line_index) + ': ', line)
#
#                     if extract_email(line) is not None:
#                         email.append(line)
#
#                     if extract_sex(line) is not None:
#                         print('Sex :', extract_sex(line))
#
#                     if extract_expertise(line) is not None:
#                         projects.append(line)
#
#                     if extract_degree(line) is not None:
#                         degrees.append(line)
#
#                     if extract_university(line) is not None:
#                         university.append(line)
#
#                     if extract_school(line) is not None:
#                         school.append(line)
#
#                     if extract_experience(line) is not None:
#                         experience.append(line)
#
#                     if extract_mobile(line) is not None:
#                         mobile.append(line)
#
#                 if extract_skills(txt) is not None:
#                     skills.append(extract_skills(txt))
#                 print('Email : ', email)
#                 print('Projects : ', projects)
#                 print('Degree : ', degrees)
#                 print('University : ', university)
#                 print('Schools : ', school)
#                 print('experience : ', experience)
#                 print('Mobile : ', mobile)
#                 print('Skills : ', skills)
#                 experience_yrs = [" "]
#                 objectives = [" "]
#
#                 ski = json.dumps(skills)
#                 exp = json.dumps(experience)
#                 pro = json.dumps(projects)
#                 expyrs = json.dumps(experience_yrs)
#                 uni = json.dumps(university)
#                 deg = json.dumps(degrees)
#                 obj = json.dumps(objectives)
#
#                 sql0 = "INSERT INTO ivm.cv_q (id,skills,Experience,projects,experience_yrs,university,degree,specialization,objectives) VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s)"
#                 val = (ivmid, ski, exp, pro, expyrs, uni, deg, deg, obj)
#                 mycursor.execute(sql0, val)
#                 mydb.commit()
#                 x='{"id1":"'+ivmid+'","skills":"'+ski+'","experience":"'+exp+'","projects":"'+pro+'","exy":"'+expyrs+'","uni":"'+uni+'","deg":"'+deg+'","obj":"'+obj+'"}'
#                 y1 = invalid_escape.sub(replace_with_byte, x)
#                 y=json.loads(y1)
#
#                 print(y[skills])
#
#             if txt is not None and len(txt) > 0:
#                 if callback is not None:
#                     callback(len(collected), file_path, txt)
#                 collected[file_path] = txt
#         elif os.path.isdir(file_path):
#             read_pdf_and_docx(file_path, collected, command_logging, callback)
#
#     return y
#
#
# def read_pdf(dir_path, collected=None):
#     if collected is None:
#         collected = dict()
#     for f in os.listdir(dir_path):
#         file_path = os.path.join(dir_path, f)
#         if os.path.isfile(file_path):
#             txt = None
#             if f.lower().endswith('.pdf'):
#                 txt = pdf_to_text(file_path)
#             if txt is not None and len(txt) > 0:
#                 collected[file_path] = txt
#         elif os.path.isdir(file_path):
#             read_pdf(file_path, collected)
#
#     return collected
