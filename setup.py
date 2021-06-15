from flask import Flask,render_template,request
from markupsafe import escape
import csv

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

def writetofile(data):
    with open('database.txt', mode='a') as database:
        name = data["name"]
        email =  data["email"]
        subject = data["subject"]
        message = data["message"]
        file = database.write(f'\n{name},{email},{subject},{message}')

def writetocsv(data):
    with open('database.csv',newline = '', mode='a') as database2:
        name = data["name"]
        email =  data["email"]
        subject = data["subject"]
        message = data["message"]
        csvwriter = csv.writer(database2, delimiter=',', quotechar='|', quoting=csv.QUOTE_MINIMAL)
        csvwriter.writerow([name,email,subject,message])

@app.route('/submit_form', methods=['POST','GET'])
def submit_form():
    if request.method =='POST':
        try:
            data = request.form.to_dict()
            writetocsv(data)
            return 'form submitted'
        except:
            return 'did not save to database'
    else:
        return 'something went wrong'