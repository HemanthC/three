from flask import Flask,render_template,request,jsonify
from flask_sqlalchemy import SQLAlchemy
from os import path
from flask_login import LoginManager
from flask_login import UserMixin
from sqlalchemy.sql import func
import json
import urllib.request
import os
db = SQLAlchemy()
DB_NAME = "database.db"

app = Flask(__name__)
app.config['SECRET_KEY'] = 'hjshjhdjah kjshkjdhjs'
app.config['SQLALCHEMY_DATABASE_URI'] = f'sqlite:///{DB_NAME}'
db.init_app(app)

class User(db.Model, UserMixin):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(150))
    subject = db.Column(db.String(150))
    
with app.app_context():
        db.create_all()


@app.route('/',methods=['GET', 'POST'])
def user():
    # if not path.exists(DB_NAME):
    #     db.create_all(app=app)
    if request.method=='POST':
       cur_name = request.form.get('name')
       cur_subject=request.form.get('subject')
       new_user = User(name=cur_name, subject=cur_subject,)
       
       db.session.add(new_user)
       db.session.commit()
       return "successfull"
    else:
       return render_template('data.html')


@app.route('/userdata',methods=['GET','POST'])
def user_data():
    if request.method=='POST':
        username=request.form.get('name')
        #userdata = User.query.filter_by(name=username)
        userdata=User.query.filter_by(name=username).first()
        
        #return json.load(jsonify(userdata))
        print(userdata)
        jdata = jsonify(name=userdata.name)
        dic = {}
        dic['name'] = userdata.name
        dic['subject']=userdata.subject
        #return render_template("user.html",content = dic)
        return dic
    else:
       return render_template('user.html')


@app.route('/database')
def database():
    users=User.query.all()
    dict={}
    for user in users:
        dic={}
        dic['name']=user.name
        dic['subject']=user.subject
        dict[user.name]=dic
        return dict

@app.route('/time')
def time():
    url = "http://127.0.0.1:3000/?api_key={}".format(os.environ.get("hjshjhdjah kjshkjdhjs"))

    response = urllib.request.urlopen(url)
    data = response.read()
    #dict = json.loads(data)
    cur_time=str(data)
    return cur_time
if __name__ == '__main__':
    app.run(debug=True)









