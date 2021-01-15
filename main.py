import os
import time


from flask import Flask, request, render_template, url_for, redirect, send_from_directory
from flask_mail import Mail, Message
from panoToVid import saveVideoFromImage


mail_settings = {
    "MAIL_SERVER": 'smtp.gmail.com',
    "MAIL_PORT": 465,
    "MAIL_USE_TLS": False,
    "MAIL_USE_SSL": True,
    "MAIL_USERNAME": "zarAppDev@gmail.com",
    "MAIL_PASSWORD": ''
}


app = Flask(__name__)
app.config.update(mail_settings)
mail = Mail(app)


@app.route('/', methods=["GET"])
def index():
    return render_template("index.html")

@app.route('/postImage', methods=["POST"])
def postImage():
    email = request.form["email"]
    id = str(int(time.time()*1000000))
    f = request.files['myfile']
    f.save("./images/" + id + ".png")
    saveVideoFromImage(id)
    emailVideo(id, email)
    return "sent u an email bb"

def emailVideo(id, email):
    msg = Message("Hello",
                  sender="zacreid45@gmail.com",
                  recipients=[email])
    with app.open_resource("./videos/"+id+".mp4") as fp:
        msg.attach("vid.mp4","video/mp4", fp.read())
    mail.send(msg)


app.run(host='0.0.0.0', port=80)
