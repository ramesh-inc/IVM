import re
from nltk.corpus import words
def extract_name(line):
    name=None
    x=line.split(' ')
    for words1 in x:
        if words1 in words.words():
            name = None
        else:
            if line.isupper()==True:
                name = line
                if name == '':
                    name = None

    return name

def extract_address(line):
        address=None
        y = line.find("address")

        if y==0:
            address=line
        else:
            address=None
        return address

def extract_nic(line):
    nic=None
    x=line.lower()
    for words1 in x:
        y=list(words1)
        if len(y)==10:
            if (y[0]==9 or y[0]==8) and (y[9]=="v" or y[9]=="V"):

                nic = words1
            else:
                nic=None
    return nic

def extract_linkedin(line):
    lurl=None

    x=line.split("/")
    for i in (x):
        # if i.find("www.linkedin.com") == 0:
        #     m = x.index("www.linkedin.com")
        #     n = m + 2
        #     lurl(x[n])
        #
        # else:
             lurl=None
    return lurl






def extract_email(line):
    email = None
    match = re.search(r'[\w\.-]+@[\w\.-]+', line)
    if match is not None:
        email = match.group(0)
        #email = [match.group(0)]


    return email


def extract_sex(parts):
    sex_found = False
    sex = None
    for w in parts:
        if 'sex' in w:
            sex_found = True
            continue
        if sex_found and ':' not in w:
            if w == 'male':
                sex = 'male'
            else:
                sex = 'female'
            break
    return sex


def extract_education(parts, line):
    found = False
    education = None
    for w in parts:
        if 'education' in w:
            found = True
            continue
        if found and ':' not in w:
            education = w
            break
    return education


def extract_mobile(line):
    phone = re.findall(re.compile(
        r'(?:(?:\+?([0-9]|[0-9][0-9]|[0-9][0-9][0-9])\s*(?:[.-]\s*)?)?(?:\(\s*([0-9][0-9]|[0-9][0-9]|[0-9][0-9][0-9])\s*\)|([0-9][1-9]|[0-9][0-9]|[0-9][0-9]|[0-9][0-9][0-9]))\s*(?:[.-]\s*)?)?([2-9]1[02-9]|[2-9][02-9]1|[2-9][02-9]{2})\s*(?:[.-]\s*)?([0-9]{4})(?:\s*(?:#|x\.?|ext\.?|extension)\s*(\d+))?'),
        line)

    if phone:
        number = ''.join(phone[0])
        if len(number) > 8:
            return '+' + number
        else:
            return None


def extract_expertise(line):
    index1=None
    line = line.lower()
    index1 =line.find('know ')
    if index1 == -1:
        index1 = line.find('familiar')
    if index1 == -1:
        index1 = line.find('knowledge ')
    if index1 == -1:
        index1 = line.find('use')
    if index1 == -1:
        index1 = line.find('master')
    if index1 == -1:
        index1 = line.find('understand')
    if index1 == -1:
        index1 = line.find('develop')

    result = None
    if index1 == -1:
        return None
    else:
        result = line[index1 :].replace(':', '').strip()
        if result == '':
            return None
    return result

def extract_otherskills(line):
    index1=None

    index1 =line.find('skill ')
    if index1 == -1:
        index1 = line.find('ability')
    if index1 == -1:
        index1 = line.find('Skills ')


    result = None
    if index1 == -1:
        return None
    else:
        result = line[index1 :].replace(':', '').strip()
        if result == '':
            return None
    return result


def extract_degree(line):
    length = 4
    line = line.lower()
    index = line.find('b.sc')
    if index == -1:
        index = line.find('hons')
    if index == -1:
        index = line.find('masters')
    if index == -1:
        index = line.find('msc')
    if index == -1:
        index = line.find('mcs')


    result = None
    if index == -1:
        return None
    else:
        result = line[index :].replace(':', '').strip()
        if result == '':
            return None
    return result

def extract_university(line):
    length = 4
    line = line.lower()
    index = line.find('institute')
    if index == -1:
        index = line.find('university')

    result = None
    if index == -1:
        return None
    else:
        result = line
        if result == '':
            return None
    return result

def extract_specialization(line):
    length = 4
    line = line.lower()
    index = line.find('specialize')
    if index == -1:
        index = line.find('specializaton')

    result = None
    if index == -1:
        return None
    else:
        result = line
        if result == '':
            return None
    return result

def extract_school(line):

    line = line.lower()
    index = line.find('school')
    if index == -1:
        index = line.find('college')



    result = None

    if (index == -1) | ('member' in line):
        return None

    else:
        result = line
        if result == '':
            return None
    return result



def extract_ethnicity(parts, line):
    race_found = False
    race = None
    for w in parts:
        if w.find('race') != -1:
            race_found = True
            continue
        if race_found and w.find(':') == -1:
            race = w
            break
    return race


# def extract_name(parts, line):
#     found = False
#     result = None
#     for w in parts:
#         if w.find('name') != -1:
#             found = True
#             continue
#         if found and w.find(':') == -1:
#             result = w
#             break
#     return result


def extract_objective(parts, line):
    found = False
    result = None
    for w in parts:
        if w.find('objective') != -1:
            found = True
            continue
        if found and ':' not in w:
            result = w
            break
    return result

def extract_experience(line):

    line = line.lower()
    index = line.find('trainee')
    if index == -1:
        index = line.find('train')
    if index == -1:
        index = line.find('worked')
    if index == -1:
        index = line.find('working')
    if index == -1:
        index = line.find('experience')
    if index == -1:
        index = line.find('years')
    if index == -1:
        index = line.find('months')


    result = None
    if index == -1:
        return None
    else:
        result = line
        if result == '':
            return None
    return result

def extract_objectives(line):

    line = line.lower()
    index = line.find('self')
    if index == -1:
        index = line.find('i ')
    if index == -1:
        index = line.find('am')



    result = None
    if index == -1:
        return None
    else:
        result = line
        if result == '':
            return None
    return result

SKILLS=['machine learning', 'ml', 'artificial intelligence', 'ai', 'natural language processing', 'nlp', 'java',  'javascript',  'php',  'c++', 'Spring',  'reactjs',  'reactnative',  'angular 2', 'maven',  'docker',  'jenkins',  'travis', 'mysql',  'mariadb', 'mongodb',
        'windows',  'linux',  'macos',  'c', 'c++',  'java',  '.net',  'mysql', 'microsoft Office',  'netBeans', 'html',
        'css',  'php','sql server data tools', 'sql', 'Server', 'Management', 'studio', 'ms sql report builder', 'excel power bi','.net']

def extract_skills(txt):
    txtn=[]
    for x in txt:
        txtn.append(x.lower())



    ski = {}
    # Extract education degree
    for index, text in enumerate(txtn):
        for tex in text.split():
            # Replace all special symbols
            tex = re.sub(r'[?|$|.|!|,]', r'', tex)
            if tex in SKILLS:
                # and tex not in STOPWORDS:
                ski[tex] = text + txtn[index + 1]

    # Extract year
    skills2 = []
    for key in ski.keys():
        skills2.append(key)
    return skills2








