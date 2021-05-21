# first create a version env, venv using py -3 -m venv venv or make the webserver2 the venv using
# py -3 -m venv web_server2
# next activate the venv using venv\Scripts\activate or web_server2\Scripts\activate
# do a pip install flask to install flask in this venv(webserver2)
# set FLASK_APP=server2.py....
# flask run
# this brings the url/addrss of my laptop
# turn on debug mode by set FLASK_ENV=development
# store css,js,asset files in static folder
# store html files in templates
# update locations, save, refresh
from flask import Flask, render_template, url_for, request, redirect
import csv

app = Flask(__name__)
print(__name__)


@app.route('/')
def my_home():
    return render_template('index.html')


# @app.route('/components.html')
# def components():
#     return render_template('components.html')

@app.route('/<string:page_name>')
def html_page(page_name):
    return render_template(page_name)


# this is never called on the front end
# search for send message on index.html, go to form above ....form action="name of new route created(submit_form)"
# method "post/get"
# put name tags in the email, subject and message sections in the html files to enable u grab the data at the backend
# save info to a write_to_csv function
@app.route('/submit_form', methods=['POST', 'GET'])
def submit_form():
    if request.method == 'POST':
        data = request.form.to_dict()
        write_to_csv(data)
        return redirect('thankyou.html')
    else:
        return 'something went wrong'


def write_to_csv(data):
    with open('mydatabase.csv', mode='a', newline='') as mydatabase:
        email = data["email"]
        subject = data["subject"]
        message = data["message"]
        csv_writer = csv.writer(mydatabase, delimiter=',', quotechar='|', quoting=csv.QUOTE_MINIMAL)
        csv_writer.writerow([email, subject, message])

# use pythonanywhere to move to the cloud
# do a repo on git hub, clone the file and move static, templates, server.py and csv files to the cloned repo
# do a pip freeze > requirements.txt to create a requirements txt with all of the requirements needed to work on any
# future machines.. instead of uploading all of the files,, we upload the requirements and some of the files and
# pythonanywhere automatically downlaods flask, jinja....
# jinja is for templating
# add requirements.txt to portfo file on github ,, then add, commit, push to main
# clone the repo on the pythonanywhere dashboard using the online console
# do an ls to see the portfo, do a cd portfo and ls to see the files in the portfo
#on python anywhere got tofiles to see ur portfo folder and its content
# go to webapp on the pythonanywhere dashboard add a new web app,, u can pay to generate a domain name
#select the python config u want(manual),
#enter portfo in the web for source code
# follow this https://help.pythonanywhere.com/pages/Flask/ install venv, flask, then u start workin on venv, set up venv
#type the name of the venv
#go to wsgi config file remove all text exept flask cos thats wat u are working on
#change path to portfo and do these
# import sys
# path = '/home/IsaacMercy/Portfo'
# if path not in sys.path:
#     sys.path.append(path)
# from server2 import app as application  # noqa
#then save

#pythonywhere has a  log to help u fish out errors

