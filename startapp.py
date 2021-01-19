from appconfig import app
from flask import request,render_template,redirect,url_for,session
from model import *
app.config['SECRET_KEY'] = "as723871jhfjhhjghfrjhfdhfg53yv4"


db.create_all()
#http://localhost:5000/app/user/register/
@app.route("/app/user/register/",methods=["GET","POST"])
def create_user():
    msg=" "
    if request.method=="POST":
        userinfo=request.form
        print('userinfo---->',userinfo["Name"])
        if userinfo:
            user=User(name=userinfo["Name"],
                  age=userinfo["Age"],
                  )
            db.session.add(user)
            db.session.commit()
            login=Login(email=userinfo["Email"],
                    password=userinfo["Password"],
                    userid=user.id)
            db.session.add(login)
            db.session.commit()
            return render_template("index.html", resp=msg)
        msg="All fields are mandatory"
    return render_template("index.html", resp=msg)


@app.route("/app/user/login/",methods=["GET","POST"])
def authanticate_user():
    msg=" "
    if request.method=="POST":
        usercredential=request.form
        email=usercredential.get('Email')
        password=usercredential.get('Password')
        login=Login.query.filter(Login.email==email,Login.password==password).first()
        if login:
            userdata=usercredential.get("Email")
            useremail=userdata.split('@')[0]
            session["user"]=useremail
            #print("userdata",userdata.split('@')[0],type(userdata))
            #msg="user {} logged in".format(useremail)
            return render_template("dashboard.html",userinfo=useremail)
        else:
            msg = "Incorrect email and password"
    return render_template("index.html",resp=msg)

if __name__ == '__main__':
    app.run(debug=True)