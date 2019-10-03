from flask import Flask, flash, request, redirect, url_for, render_template
import math

from dbModule import sq_user as userClass
from dbModule import sq_cv_q_predict as cvPredict
from dbModule import sq_vacancy_matching as vm
from dbModule import sq_company as company
from dbModule import sq_vacancies as vacancies
from dbModule import sq_anonimity as anonimity
import nbPrediction as Predictor
import vacancyMatching as vMatcher

# Imports of Maddhushani
import datetime
import json
import os
import subprocess
import time
from PIL import Image
from flask import Flask, flash, request, redirect, url_for, render_template
from flask import send_from_directory
from pytesseract import pytesseract
from requests import session
from werkzeug.utils import secure_filename
from utility.pdf_utils import pdf_to_text
from utility.docx_utils import docx_to_text
from utility.parser_rules import *
import mysql
import sys
import spacy
from utility.docx_utils import docx_to_text
from linkedin_api import Linkedin
from ivmvacancy import extract_education, extract_skills2, extract_job

import mysql.connector

from extraction.utility.parser_rules import extract_sex, extract_email, extract_otherskills, extract_experience, \
    extract_degree, extract_university, extract_school

mydb = mysql.connector.connect(
    host="localhost",
    user="root",
    passwd="",
    database="ivm-madhushani"
)
mydb1 = mysql.connector.connect(
    host="localhost",
    user="root",
    passwd="",
    database="ivm-madhushani"
)
mycursor = mydb.cursor()
mycursor1 = mydb1.cursor()

nlp = spacy.load('en_core_web_sm')
sys.path.append(os.path.join(os.path.dirname(__file__), '..'))

UPLOAD_FOLDER = 'data'
ALLOWED_EXTENSIONS = {'txt', 'pdf', 'doc', 'docx'}
ALLOWED_EXTENSIONS1 = {'png', 'jpg', 'jpeg','jpg'}
# End of Import of Madhushani

app = Flask(__name__, template_folder='frontend', static_folder='frontend')
app.secret_key = 'super secret key'

app.config['SESSION_TYPE'] = 'filesystem'
app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER

# get file extention and check whether the file is allowed
def allowed_file(filename):
    return '.' in filename and \
           filename.rsplit('.', 1)[1].lower() in ALLOWED_EXTENSIONS


def allowed_file1(filename):
    return '.' in filename and \
           filename.rsplit('.', 1)[1].lower() in ALLOWED_EXTENSIONS1

#Route to Home Page
@app.route('/', methods=['GET', 'POST'])
def home():
    return render_template('index.html')


#Route to fill RESUME FORM
@app.route("/resume_details", methods=['GET', 'POST'])
def resume_details():
    return render_template('resume_details.html')


#Submit resume upload
@app.route("/upload_resume", methods=['GET', 'POST'])
def upload_resume():
    if request.method == 'POST':

        # Resume Details
        name = request.form['name']
        email = request.form['email']
        address = request.form['address']
        age = request.form['age']
        university = request.form['university']
        nic = request.form['nic']
        degree = request.form['degree']
        specialization = request.form['specialization']
        exp_yrs = request.form['exp_yrs']
        skills = request.form['skills']
        phone = request.form['phone']

        # Anonimity Details
        a_name = request.form['a_name']
        a_email = request.form['a_email']
        a_address = request.form['a_address']
        a_nic = request.form['a_nic']
        a_phone = request.form['a_phone']

        # Save the comment here.
        print("Personal Details")
        print('Name: ' + name)
        print('Email: ' + email)
        print('Phone: ' + phone)
        print('Address: ' + address)
        print('Age: ' + age)
        print('University: ' + university)
        print('NIC: ' + nic)
        print('Degree: ' + degree)
        print('Specialization: ' + specialization)
        print('Experience Years: ' + exp_yrs)
        print('skills: ' + skills)
        print("======================================")

        print("Anonimity Level")
        print('Anonimity Value for Name: ' + a_name)
        print('Anonimity Value for Email: ' + a_email)
        print('Anonimity Value for Phone: ' + a_phone)
        print('Anonimity Value for Address: ' + a_address)
        print('Anonimity Value for NIC: ' + a_nic)
        print("======================================")

        projects = ''
        obj = ''

        # Anonymize Values
        if(int(a_name) != 0):
            anonimized_name = name.replace(name[0:math.ceil((int(len(name)-1) * int(a_name)) / 10):], "XXX")
        else:
            anonimized_name = name

        if(int(a_address) != 0):
            anonimized_address = address.replace(address[0:math.ceil((int(len(address)-1) * int(a_address)) / 10):], "XXX")
        else:
            anonimized_address = address

        if(int(a_nic)!= 0):
            anonimized_nic = nic.replace(nic[0:math.ceil((int(len(nic)-1) * int(a_nic)) / 10):], "XXX")
        else:
            anonimized_nic = nic

        if(int(a_email) != 0):
            anonimized_email = email.replace(email[0:math.ceil((int(len(email)-1) * int(a_email)) / 10):], "XXX")
        else:
            anonimized_email = email

        if(int(a_phone) != 0):
            anonimized_phone = phone.replace(phone[0:math.ceil((int(len(phone)-1) * int(a_phone)) / 10):], "XXX")
        else:
            anonimized_phone = phone

        userid = userClass.user().insertUser(age, name, address, nic, email, phone)
        cvPredict.cv_q_predict().insertPredictionData(userid, age, skills, projects, exp_yrs, university, degree, specialization, obj)
        anonimity.anonimity().insertAnonimity(userid, anonimized_name, anonimized_address, anonimized_nic, anonimized_email, anonimized_phone)

        Predictor.Prediction().makePredictionNb()
        vacancy_matching = vm.sq_vacancy_matching().selectByResumeID(userid)

        print("Vacancy_matching" + str(vacancy_matching))

        # Build Suggestion Result
        matching_vacancyList = list()

        for row in vacancy_matching:
            vacancyList = vacancies.sq_vacancies().selectVacancies(row[2])
            matching_vacancyList.append(vacancyList)

        print(matching_vacancyList)

        print("======================================")

        return render_template('suggestion_vacancy.html', vacancyListParam = matching_vacancyList)

    else:
        return render_template('resume_details.html')
    return render_template('resume_details.html')


#Route to fill VACANCY FORM
@app.route("/vacancy_details", methods=['GET', 'POST'])
def vacancy_details():
    return render_template('vacancy_details.html')


#Submit Vacancy Upload
@app.route("/upload_vacancy", methods=['GET', 'POST'])
def upload_vacancy():
    if request.method == 'POST':

        # Vacancy Details
        name = request.form['name']
        email = request.form['email']
        address = request.form['address']
        phone = request.form['phone']
        job_type = request.form['job_type']
        job_title = request.form['job_title']
        edu_qualification = request.form['edu_qualification']
        exp_technologies = request.form['exp_technologies']
        exp_yrs = request.form['exp_yrs']
        required_skills = request.form['required_skills']
        other_skills = request.form['other_skills']

        # Display Resume Details
        print("Company Details")
        print('Company Name: ' + name)
        print('Company Email: ' + email)
        print('Company Phone: ' + phone)
        print('Company Address: ' + address)
        print('Company Job Type: ' + job_type)
        print('Company Job Title: ' + job_title)
        print('Required Education Qualification: ' + edu_qualification)
        print('Experienced Technologies: ' + exp_technologies)
        print('Required Skills: ' + required_skills)
        print('Required Experience Years: ' + exp_yrs)
        print('Other Skills: ' + other_skills)
        print("======================================")

        companyId = company.company().insertCompany(name, address, phone, email, job_type)
        vacancyId = vacancies.sq_vacancies().insertVacancy(companyId, job_title, edu_qualification, exp_technologies, exp_yrs, required_skills, other_skills)
        vMatcher.VacancyMatching().matchingByVacencyId(vacancyId)

        print(companyId)
        matchingDetails = vm.sq_vacancy_matching().selectByVacancyID(vacancyId)


        # Build Suggestion Result
        candidates = list()
        anonimityList = list()

        for row in matchingDetails:
            user = userClass.user().selectUser(row[1])
            anonimityValues = anonimity.anonimity().selectByUserID(row[1])
            candidates.append(user)
            anonimityList.append(anonimityValues)

        print(candidates)
        print(anonimityList)

    else:
        return render_template('suggetion_resume.html')
    return render_template('suggetion_resume.html', candidates=anonimityList)


#Get Resumes for Vacancy
@app.route("/build_resume_list", methods=['GET', 'POST'])
def build_resume_list():
    if request.method == 'POST':
        vacancyId = request.form['vacancy_id']
        vMatcher.VacancyMatching().matchingByVacencyId(vacancyId)

        print("Vacancy Id: " + vacancyId)
        matchingDetails = vm.sq_vacancy_matching().selectByVacancyID(int(vacancyId))
        print("Matching Details: " + str(matchingDetails))


        # Build Suggestion Result
        candidates = list()
        anonimityList = list()

        for row in matchingDetails:
            user = userClass.user().selectUser(row[1])
            print(row[1])
            anonimityValues = anonimity.anonimity().selectByUserID(row[1])
            candidates.append(user)
            print(anonimityValues)
            anonimityList.append(anonimityValues)

        print(candidates)
        print(anonimityList)

    else:
        return render_template('suggetion_resume.html')
    return render_template('suggetion_resume.html', candidates=anonimityList)


# Madhushani

# get signup/Sign In page after clicking sign in button in home page
@app.route('/signup', methods=['GET', 'POST'])
def loadpage():
    return render_template('joinivm.html')


# get data extraction page after uploading job seekers' cv to the system in signup page
# select file and upload to the data folder
@app.route('/upload', methods=['GET', 'POST'])
def upload_file():
    if request.method == 'POST':
        # check if the post request has the file part
        if 'file' not in request.files:
            flash('No file part', 'warning')
            # return redirect(url_for('index'))
        file = request.files['file']
        # if user does not select file, browser also
        # submit an empty part without filename
        if file.filename == '':
            flash('No selected file', 'warning')
        # return redirect(url_for('index'))
        if file:
            flash('Please select pdf/doc/docx/txt')
            # return redirect(url_for('index'))
        if file and allowed_file(file.filename):
            filename = secure_filename(file.filename)
            print(filename)
            os.chmod(UPLOAD_FOLDER, 0o777)
            os.access('data', os.W_OK)  # Check for write access
            os.access('my_folder', os.R_OK)
            file.save(os.path.join(app.config['UPLOAD_FOLDER'], filename))
            # return redirect('exx',file_name=filename)
            # send_from_directory(app.config['UPLOAD_FOLDER'], filename)
            return redirect(url_for('extracted', filename=filename))

    return render_template('joinivm.html')


# extract file from docx  or pdf
# identify fields
# assign identified values to text fields
# store data in data base
@app.route('/extract/<filename>', methods=['GET', 'POST'])
def extracted(filename):
    file_path = (os.path.join(app.config['UPLOAD_FOLDER'], filename))
    if os.path.isfile(file_path):
        txt = None
        # extract file from .docx format
        if file_path.lower().endswith('.docx'):

            print('extracting text from docx: ', file_path)
            txt = docx_to_text(file_path)
            print(txt)
            ivmid = datetime.datetime.now().strftime("%I:%M%p%B%d%Y").replace(":/ ", "")
            name1 = []
            address = []
            linkedin = []
            nic = []
            email = []
            projects = []
            degrees = []
            university = []
            school = []
            experience = []
            mobile = []
            skills = []
            name = []
            for line_index, line in enumerate(txt):
                # print('Line #' + str(line_index) + ': ', line)
                # if extract_name(line) is not None:
                #     name1.append(line)

                if extract_address(line) is not None:
                    address.append(line)

                if extract_nic(line) is not None:
                    nic.append(line)

                # if extract_linkedin(line) is not None:
                #     linkedin.append(line)

                if extract_email(line) is not None:
                    email.append(line)

                if extract_sex(line) is not None:
                    print('Sex :', extract_sex(line))

                if extract_expertise(line) is not None:
                    projects.append(line)

                if extract_degree(line) is not None:
                    degrees.append(line)

                if extract_university(line) is not None:
                    university.append(line)

                if extract_school(line) is not None:
                    school.append(line)

                if extract_experience(line) is not None:
                    experience.append(line)

                if extract_mobile(line) is not None:
                    mobile.append(line)

            if extract_skills(txt) is not None:
                skills.append(extract_skills(txt))
            print('Email : ', email)
            print('Projects : ', projects)
            print('Degree : ', degrees)
            print('University : ', university)
            print('Scools : ', school)
            print('experience : ', experience)
            print('Mobile : ', mobile)
            print('Skills : ', skills)
            experience_yrs = [" "]
            objectives = [" "]

            nam = json.dumps(name1, ensure_ascii=False)
            add = json.dumps(address, ensure_ascii=False)
            lin = json.dumps(linkedin, ensure_ascii=False)
            nic1 = json.dumps(nic, ensure_ascii=False)
            ski = json.dumps(skills, ensure_ascii=False)
            exp = json.dumps(experience, ensure_ascii=False)
            pro = json.dumps(projects, ensure_ascii=False)
            expyrs = json.dumps(experience_yrs, ensure_ascii=False)
            uni = json.dumps(university, ensure_ascii=False)
            deg = json.dumps(degrees, ensure_ascii=False)
            obj = json.dumps(objectives, ensure_ascii=False)
            print(ski)

        # extract data from pdf

        elif file_path.lower().endswith('.pdf'):

            print('extracting text from pdf: ', file_path)

            txt = pdf_to_text(file_path)
            print(txt)
            name1 = []
            address = []
            linkedin = []
            nic = []
            email = []
            projects = []
            degrees = []
            university = []
            school = []
            experience = []
            mobile = []
            skills = []
            name = []
            for line_index, line in enumerate(txt):

                if extract_address(line) is not None:
                    address.append(line)

                if extract_nic(line) is not None:
                    nic.append(line)

                if extract_linkedin(line) is not None:
                    linkedin.append(line)

                if extract_email(line) is not None:
                    email.append(line)

                if extract_sex(line) is not None:
                    print('Sex :', extract_sex(line))

                if extract_expertise(line) is not None:
                    projects.append(line)

                if extract_degree(line) is not None:
                    degrees.append(line)

                if extract_university(line) is not None:
                    university.append(line)

                if extract_school(line) is not None:
                    school.append(line)

                if extract_experience(line) is not None:
                    experience.append(line)

                if extract_mobile(line) is not None:
                    mobile.append(line)

            if extract_skills(txt) is not None:
                skills.append(extract_skills(txt))
            print('Email : ', email)
            print('Projects : ', projects)
            print('Degree : ', degrees)
            print('University : ', university)
            print('Schools : ', school)
            print('experience : ', experience)
            print('Mobile : ', mobile)
            print('Skills : ', skills)
            experience_yrs = " "
            objectives = [" "]

            nam = json.dumps(name1)
            add = json.dumps(address)
            lin = ""
            nic1 = json.dumps(nic)
            ski = json.dumps(skills)
            exp = json.dumps(experience)
            pro = json.dumps(projects)
            expyrs = json.dumps(experience_yrs)
            uni = json.dumps(university)
            deg = json.dumps(degrees)
            obj = json.dumps(objectives)

        # get edited data from the form and save to db

        if request.method == 'POST':
            namer = re.sub(r"[\n\t\s]*", "", (request.form['full_name']))
            mobiler = (request.form['phone_number'])
            addressr = (request.form['address'])
            emailr = (request.form['email'])
            nicr = (request.form['nic'])
            unir = (request.form['university'])
            degr = (request.form['degree'])
            schr = (request.form['school'])
            skir = json.dumps(request.form['skills'], ensure_ascii=False)
            expr = (request.form['experience'])
            pror = (request.form['projects'])
            spr = (request.form['specialization'])
            url1 = (request.form['linkedin_link'])
            # url1 = json.dumps(request.form['linkedin_link'], ensure_ascii=False)

            # sname = int(request.form['sname'])
            # sphone = int(request.form['sphone'])
            # saddress = int(request.form['saddress'])
            # semail = int(request.form['semail'])
            # snic = int(request.form['snic'])

            # namenum = round((len(namer) / 10)) * sname
            # print(namenum)
            # emailnum = round((len(emailr) / 10)) * semail
            # addressnum = round((len(addressr) / 10)) * saddress
            # phonenum = round((len(mobiler) / 10)) * sphone
            # nicnum = round((len(nicr) / 10)) * snic

            # AC = input("What is your Preferred Privacy Level: 1- Fully Anonymized   2- Partially Anonymized    3- Totally Visible :")

            # aname1 = namer[:(len(namer)) - namenum], ("xxxx")
            # aemail1 = emailr[:len(emailr) - emailnum]
            # aaddress1 = addressr[:len(addressr) - addressnum]
            # aphone1 = mobiler[:len(mobiler) - phonenum]
            # anic1 = nicr[:len(nicr) - nicnum]
            job = "Software Engineer"
            age = 25
            nbstatus = 0
            dtstats = 0

            # Anonimity Details
            a_name = request.form['a_name']
            a_email = request.form['a_email']
            a_address = request.form['a_address']
            a_nic = request.form['a_nic']
            a_phone = request.form['a_phone']

            sql_user = "insert into user(age, name, address,nic, email, phone,  experience) values(%s, %s, %s, %s, %s, %s,%s)"

            val_user = (age, namer, addressr, nicr, emailr, mobiler, expr)
            mycursor.execute(sql_user, val_user)
            mydb.commit()
            ivmid = mycursor.lastrowid

            print("Anonimity Level")
            print('Anonimity Value for Name: ' + a_name)
            print('Anonimity Value for Email: ' + a_email)
            print('Anonimity Value for Phone: ' + a_phone)
            print('Anonimity Value for Address: ' + a_address)
            print('Anonimity Value for NIC: ' + a_nic)
            print("======================================")

            projects = ''
            obj = ''

            # Anonymize Values
            if (int(a_name) != 0):
                anonimized_name = namer.replace(namer[0:math.ceil((int(len(namer) - 1) * int(a_name)) / 10):], "XXX")
            else:
                anonimized_name = namer

            if (int(a_address) != 0):
                anonimized_address = addressr.replace(addressr[0:math.ceil((int(len(addressr) - 1) * int(a_address)) / 10):], "XXX")
            else:
                anonimized_address = addressr

            if (int(a_nic) != 0):
                anonimized_nic = nicr.replace(nicr[0:math.ceil((int(len(nicr)) * int(a_nic) - 1) / 10):], "XXX")
            else:
                anonimized_nic = nicr

            if (int(a_email) != 0):
                anonimized_email = emailr.replace(emailr[0:math.ceil((int(len(emailr) - 1) * int(a_email)) / 10):], "XXX")
            else:
                anonimized_email = emailr

            if (int(a_phone) != 0):
                anonimized_phone = mobiler.replace(mobiler[0:math.ceil((int(len(mobiler) - 1) * int(a_phone)) / 10):], "XXX")
            else:
                anonimized_phone = mobiler

            anonimity.anonimity().insertAnonimity(ivmid, anonimized_name, anonimized_address, anonimized_nic, anonimized_email, anonimized_phone)

            sql_cv_q_predict = "insert into cv_q_predict(userid, age, skills, projects,experience_yrs, university, degree,  specialization,objectives) values(%s, %s, %s, %s, %s, %s, %s,%s, %s)"

            val_cv_q_predict = (ivmid, age, skir, pror, experience_yrs, unir, degr, spr, obj)
            mycursor.execute(sql_cv_q_predict, val_cv_q_predict)
            mydb.commit()

            return redirect(
                url_for('linkedinextract', id=ivmid, url11=url1, aname=anonimized_name, aemail=anonimized_email, aaddress=anonimized_address,
                        aphone=anonimized_phone, anic=anonimized_nic, dname=namer, dmobile=mobiler, daddress=addressr, duni=unir,
                        ddeg=degr, dskills=skir, dexp=expr, dproject=pror))

    return render_template('extracted.html', skillsx=ski, namex=nam, emailx=email, projectsx=pro, degreesx=deg,
                           universityx=uni, schoolx=school, experiencex=exp, mobilex=mobile, addressx=add,
                           linkedinx=lin, nicx=nic1, arname=name1, lenname=len(name1), araddress=address,
                           lenaddress=len(address), arlinkedin=linkedin, lenlinkedi=len(linkedin),
                           arnic=nic, lennic=len(nic), aremail=email, lenemail=len(email), arproject=projects,
                           lenproject=len(projects), ardegree=degrees, lendegree=len(degrees),
                           aruniversity=university, lenuniversity=len(university), arschool=school,
                           lenschool=len(school), arexperience=experience,
                           lenexperience=len(experience), armobile=mobile, lenmobile=len(mobile), arskills=skills,
                           lenskills=len(skills))


@app.route('/saved', methods=['GET', 'POST'])
def data():
    if request.method == 'POST':
        namer = (request.form['finalname']).replace("\',\n,\t", "")
        print(namer)


# Company registation in signup page
@app.route('/creg', methods=['GET', 'POST'])
def reg():
    if request.method == 'POST':
        namer = request.form['cname']
        mobiler = request.form['cphone']
        addressr = request.form['caddress']
        emailr = request.form['cemail']
        category = request.form['ccategoty']
        password = request.form['cpassword']
        # cid = (namer + datetime.datetime.now().strftime("%I:%M%p%B%d%Y")).replace(":/ " , "")

        sql_company = "INSERT INTO company (company_name,address,phone,email,password) VALUES (%s, %s, %s,%s, %s)"
        val_company = (namer, addressr, mobiler, emailr, password)
        mycursor.execute(sql_company, val_company)
        mydb.commit()
        cid = mycursor.lastrowid
        return redirect(url_for('clogin'))

    return render_template('joinivm.html')


# Company login in signup page
@app.route('/clog', methods=['GET', 'POST'])
def clogin():
    if request.method == 'POST':
        username11 = (request.form['uemail'])
        password11 = (request.form['upassword'])
        # company login
        mycursor.execute("SELECT * from company where email=%s AND password=%s", [username11, password11])
        account = mycursor.fetchone()

        print("Return values: " + str(account))

        if account:
            pid = str(account[0])
            print("id: " + pid)

            return redirect(url_for('profileload1', id2=pid))
        # CV login
        else:
            mycursor.execute("SELECT * from cv_reg where email=%s AND password=%s;", [username11, password11])
            account = mycursor.fetchone()
            if account:
                # Create session data, we can access this data in other routes
                userid = (account[0])

                Predictor.Prediction().makePredictionNb()
                vacancy_matching = vm.sq_vacancy_matching().selectByResumeID(userid)

                # Build Suggestion Result
                matching_vacancyList = list()

                for row in vacancy_matching:
                    vacancyList = vacancies.sq_vacancies().selectVacancies(row[2])
                    matching_vacancyList.append(vacancyList)

                print("Matching Vacancy List: " + str(matching_vacancyList))

                print("======================================")

                return render_template('suggestion_vacancy.html', vacancyListParam=matching_vacancyList)

            else:
                # Account doesnt exist or username/password incorrect
                msg = 'Incorrect username/password!'

    return render_template('joinivm.html')


# get company profile page after login
ar = []


@app.route('/company/<id2>', methods=['GET', 'POST'])
def profileload1(id2):
    ar.append(id2)
    id1 = request.args.get('id2')
    print('Profile Load Id: ' + str(id2))
    mycursor.execute("SELECT * from vacancies where company_id='%s'", id1)
    values1 = mycursor.fetchall()
    for i in values1:
        print(i[0])
    if request.method == 'POST':

        # check if the post request has the file part
        if 'file' not in request.files:
            flash('No file part', 'warning')
            # return redirect(url_for('index'))
        file = request.files['file']
        # if user does not select file, browser also
        # submit an empty part without filename
        if file.filename == '':
            flash('No selected file', 'warning')
            # return redirect(url_for('index'))
        if file:
            flash('Please select png/jpg/jpeg')
            # return redirect(url_for('index'))
        if file and allowed_file1(file.filename):
            filename = secure_filename(file.filename)
            print(filename)
            # os.chmod(UPLOAD_FOLDER, 0o777)
            # os.access('data', os.W_OK)  # Check for write access
            # os.access('my_folder', os.R_OK)
            file.save(os.path.join(app.config['UPLOAD_FOLDER'], filename))
            # return redirect('exx',file_name=filename)
            # send_from_directory(app.config['UPLOAD_FOLDER'], filename)
            return redirect(url_for('extracteddetails', id=id, filename=filename))

    return render_template("vacancy.html", data=values1)


# extract vacancy details
@app.route('/excompany/<filename>', methods=['GET', 'POST'])
def extracteddetails(filename):
    c_id = ar[0]
    mycursor.execute("SELECT * from vacancies where company_id='%s'" % c_id)
    values1 = mycursor.fetchall()
    # vid = datetime.datetime.now().strftime("%I:%M%p%B%d%Y").replace(":/ ", "") + filename
    pytesseract.tesseract_cmd = r'C:\Program Files\Tesseract-OCR\tesseract.exe'
    text = pytesseract.image_to_string(Image.open((os.path.join(app.config['UPLOAD_FOLDER'], filename))), lang='eng')
    txt = []
    for line in text.split('\n' or '   ' or '. ' or ','):
        line2 = line.strip()
        if line2 != '':
            txt.append(line2)
    print(txt)
    otherskills = []
    # education = []
    # skills = []
    experience = []
    for lineindex, line in enumerate(txt):

        if extract_otherskills(line) is not None:
            otherskills.append(line)

        # if extract_education(line) is not None:
        #     education.append(line)

        # if extract_skills(line) is not None:
        #     skills.append(line)

        experience = []
        if extract_experience(line) is not None:
            experience.append(line)

    job = extract_job(text)
    skills = extract_skills2(text)
    education = extract_education(text)

    vjob = json.dumps(job)
    ved = json.dumps(education)
    vsk = json.dumps(skills)
    vos = json.dumps(otherskills)
    vex = json.dumps(experience)

    if request.method == 'POST':
        jobv = json.dumps(request.form['vjob'])
        eduv = json.dumps(request.form['vedu'])
        expv = json.dumps(request.form['vexp'])
        eyv = json.dumps(request.form['vey'])
        vskv = json.dumps(request.form['vski'])
        osv = json.dumps(request.form['voski'])
        sql_vacancies = "INSERT INTO vacancies (company_id, job, education, experience, ex_year,skills,other_skills) VALUES(%s,%s,%s,%s,%s,%s,%s) "
        val_vacancies = (c_id, jobv, eduv, expv, eyv, vskv, osv)
        mycursor.execute(sql_vacancies, val_vacancies)
        mydb.commit()
        vid = mycursor.lastrowid
        print("VID: " + str(vid))
        vMatcher.VacancyMatching().matchingByVacencyId(vid)
        flash("successfully saved")
        return render_template("vacancy.html", data=values1, vvid=c_id)

    return render_template('vacancyextract.html', vvjob=vjob, vved=ved, vvsk=vsk, vvos=vos, vvex=vex)


##############################################################
#############Testing##########################################
##############################################################
@app.route('/linkedin/<id>', methods=['GET', 'POST'])
def linkedinextract(id):
    url11 = request.args.get('url11')
    anna = request.args.get('aname')
    anem = request.args.get('aemail')
    anad = request.args.get('aaddress')
    anph = request.args.get('aphone')
    anni = request.args.get('anic')
    skills1 = request.args.get('dskills')
    name1 = request.args.get('dname')
    projects1 = request.args.get('dproject')
    degree1 = request.args.get('ddeg')
    univercity1 = request.args.get('duni')
    experience11 = request.args.get('dexp')
    phone1 = request.args.get('dmobile')
    address1 = request.args.get('daddress')
    nic1 = request.args.get('daddress')

    print(url11)
    lname = []
    lskills = []
    lexperience = []
    ldegree = []
    luniversity = []
    lemail1 = []
    lmobile = []
    # try:
    url11 = 'ravindu-landekumbura-19950214'
    linkedin1 = Linkedin('slttc.info@gmail.com', 'net@telecom')
    linkprofile = linkedin1.get_profile(url11)
    print(linkprofile)

    contact = linkedin1.get_profile_contact_info(url11)
    print(contact)
    lname = []
    lname1o = linkprofile['firstName']
    lname.append(json.dumps(lname1o))

    # lname="Ravindu landekumbura"

    lskills = []
    skills = (linkprofile['skills'])
    for skill in skills:
        z = skill['name']
        ls = json.dumps(z)
        lskills.append(ls)

    lexperience = []

    experience1 = (linkprofile['experience'])
    for ex in experience1:
        z = ex['companyName'], ex['title']
        d = json.dumps(z)
        lexperience.append(d)

    university1 = (linkprofile['education'])
    print(university1)
    luniversity = []
    ldegree = []
    for sch in university1:
        school = sch['school']
        print(school)

        nm = school['schoolName']
        luniversity.append(nm)
        dm = sch['degreeName']
        ldegree.append(dm)
    lluniversity = json.dumps(luniversity)
    lldegree = json.dumps(ldegree)
    lexperience1 = json.dumps(experience1)
    llskills = json.dumps(lskills)
    lemail1 = json.dumps(contact['email_address'])
    lmobile = json.dumps(contact['phone_numbers'])

    # except:
    print('cannot connect')

    mycursor.execute("SELECT email from user where id=%s;", [id])
    rows = mycursor.fetchall()
    for ele in rows:
        email1 = json.dumps(ele[0]).replace('[]', "")

    if request.method == 'POST':
        uid = id
        uemail = request.form['uemail']
        upassword = request.form['upassword']

        sql2 = "INSERT INTO cv_reg (id,email,password) VALUES (%s, %s, %s)"
        val = (uid, uemail, upassword)
        mycursor.execute(sql2, val)
        mydb.commit()
        return redirect(url_for('clogin', id1=uid, nameu=uemail, passu=upassword))

    return render_template('linkedin.html', urlx=url11, skillsx=skills1, namex=name1, emailx=email1,
                           projectsx=projects1, degreesx=degree1, universityx=univercity1, experiencex=experience11,
                           mobilex=phone1, addressx=address1, linkedinx=url11, nicx=nic1, namexx=lname,
                           skillsxx=llskills, experiencexx=lexperience, unversityxx=lluniversity, degreexx=lldegree,
                           emailxx=lemail1, mobilexx=lmobile, aname=anna, aemail=anem, aaddress=anad, aphone=anph,
                           anic=anni, ski=lskills,
                           len=len(lskills))

if __name__ == '__main__':
    app.run(debug=True)