from flask import Flask, render_template, request, url_for, redirect
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy.sql import func
from MySQLdb import connect
from datetime import datetime





app = Flask(__name__,template_folder='template')
app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql://root@localhost/codeing'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = True
db = SQLAlchemy(app)
# app.config['MYSQL_HOST']='localhost'
# app.config['MYSQL_USER']='root'
# app.config['MYSQL_PASSWORD']=''
# app.config['MYSQL_DB']='codeing'
# mysql=MySQL(app)



# ,instance_relative_config=True

class Contacts(db.Model):
    '''
    sno, name, phone_num, msg, date, email
    '''
    sno = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(80), nullable=False)
    phone_num = db.Column(db.String(12), nullable=False)
    msg = db.Column(db.String(120), nullable=False)
    date = db.Column(db.String(12), nullable=True)
    email = db.Column(db.String(20), nullable=False)

# class Posts(db.Model):
#     sno = db.Column(db.Integer, primary_key=True)
#     title = db.Column(db.String(80), nullable=False)
#     slug = db.Column(db.String(21), nullable=False)
#     content = db.Column(db.String(120), nullable=False)
#     date = db.Column(db.String(12), nullable=True)
# #   img_file = db.Column(db.String(12), nullable=True)

@app.route("/")
def home():
    return render_template('index.html')

# @app.route("/dashboard")
# def dashboard():
#     return render_template("index.html")


@app.route("/about")
def about():
    return render_template('about.html')

# @app.route('/post/<string:post_slug>', methods=['GET'])
# def post_route(post_slug):
#     post = Posts.query.filter_by(slug=post_slug).first()
#     return render_template('post.html',post=post)

@app.route("/post")
def post():
    return render_template('post.html')


@app.route("/contact", methods = ["GET", "POST"])
def contact():
    # print("calling")
    if(request.method=="POST"):
        '''Add entry to the database'''
        name = request.form.get('name')
        # print(name)
        email = request.form.get('email')
        phone= request.form.get('mobile')
        message = request.form.get('message')
        entry = Contacts(name=name, phone_num= phone, msg = message, date= datetime.now(),email = email )
        db.session.add(entry)
        db.session.commit()
        
    return render_template('contact.html')
   

app.run(debug=True)


