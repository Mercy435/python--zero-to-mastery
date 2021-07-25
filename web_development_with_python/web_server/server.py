'''
from flask import Flask

app = Flask(__name__)  # an instance from Flask
print(__name__)


# frame works give higher level of abstraction
@app.route('/')  # a decorator
def hello_world():
    return 'Hello!!!!!!!'


# creating a blog route
@app.route('/blog')  # creating another root with a/blog on the website
def blog():
    return 'These are my thoughts on blogs'


@app.route('/blog/2020/dogs')  # we can have multiple routes
def blog2():
    return 'this is my dog'


# to send html files instead of text strings add another module render_template from flask
import os
from flask import Flask, render_template, url_for

app = Flask(__name__)


@app.route('/<username>/<int:post_id>/')  # passes a username, post_id(int) with the home page
def hello_world(username=None, post_id=None):
    # print(url_for('static', filename='favicon.ico'))
    return render_template('index.html',
                           name=username, post_id=post_id)  # flask looks for a folder called templates to search for the html file


# so put ur html file in a folder titled accordingly
# templates are used to add multiple html files

@app.route('/about.html')
def about():
    return render_template('about.html')

# create a static folder so the flask app knows to look into it for css and js files, then change their path in the html
# file

# @app.route('/favicon.ico')
# def blog():
#     return 'These are my thoughts on blogs'
'''
# adding a favicon




# for my portfolio
from flask import Flask, render_template, request, redirect, send_from_directory
import csv
import os

#
app = Flask(__name__)
print(__name__)


@app.route('/')
def my_home():
    return render_template('index.html')


@app.route('/static/assets/favicon.ico')
def favicon():
    return send_from_directory(os.path.join(app.root_path, 'static'),
                               'favicon.ico')
#
# @app.route('/about.html')
# def about():
#     return render_template('about.html')
#
#
# @app.route('/works.html')
# def works():
#     return render_template('works.html')
# to avoid repetition of codes for each site, use the url parameter<string: page_name at the home page
# to automate any html page

# this automates 75-81
@app.route('/<string:page_name>')
def html_page(page_name):
    return render_template(page_name)


# for file uploads
# get means browser wants us to send info and post is to saveinfo sent to server
# this is for backend,it is never called on the front end(browser)
# do method = post and submit_form at the action attribute, form tag in the contact.html
# this helps us capture the data user sends to the server
@app.route('/submit_form', methods=['POST', 'GET'])
def submit_form():
    # return 'form submitted hoorayyy!'
    if request.method == 'POST':
        try:
            data = request.form.to_dict()
            # print(data)  # prints dict of data on the terminal
            # write_to_file(data)  # to save data in text database
            write_to_csv(data)
            return redirect('/thankyou.html')  # this route
        except:
            return 'did not save to database'
    else:
        return 'something went wrong. Try again!'


# adding a name variable to all inputs(email,text,textarea) at the contact.html to enable the server read the data, so
# we can grab the data at the backend  note that the inputs all have the same class
# in the developers tool we now see the form data cos we gave it name attributes.... its an html standard

# to print a thankyou at the end, duplicate the contact,html and name it thankyou.html
# close up the form tag(62-110) erase them and write a thank you message
# we redirect to the thank you page after contact has been submitted by importing redirect module in line 1054



# SAVING INPUT DATA SO IT IS NOT LOST
# create a text file called database to store info the server receives
# databases are a way to store data in a safe way , away from the server
def write_to_file(data):
    with open('database.txt', mode='a') as database:  # a to append
        email = data["email"]
        subject = data["subject"]
        message = data["message"]
        file = database.write(f"\n{email},{subject},{message}")  # \n for new line anytime we get an entry


# using python csv module to write and save as it is better than txt
def write_to_csv(data):
    with open('database.csv', mode='a', newline='') as database2:  # a to append
        email = data["email"]
        subject = data["subject"]
        message = data["message"]
        csv_writer = csv.writer(database2, delimiter=',', quotechar='|', quoting=csv.QUOTE_MINIMAL)
        csv_writer.writerow([email, subject, message])
#local hosthttp://127.0.0.1:5000/ my computer

#pythin anywhere is used to host your website