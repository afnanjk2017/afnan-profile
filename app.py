import os
import re

from flask_mail import Mail, Message
from flask import Flask, flash, render_template, request


# Configure application
app = Flask(__name__)

# Ensure templates are auto-reloaded
app.config["TEMPLATES_AUTO_RELOAD"] = True


app.config['SECRET_KEY'] = 'r3t058rf3409tyh2g-rwigGWRIGh[g'
app.config["MAIL_PASSWORD"] = os.environ["MAIL_PASSWORD"]
app.config["MAIL_USERNAME"] = "afnanjk2017@gmail.com"
app.config["MAIL_PORT"] = 587
app.config["MAIL_SERVER"] = "smtp.gmail.com"
app.config["MAIL_USE_TLS"] = True


mail = Mail(app)




@app.route("/")
def layout():
     return render_template("layout.html")


@app.route("/skills")
def skills():
    return render_template("skills.html")

@app.route("/apps")
def apps():
    return render_template("apps.html")



@app.route("/contact", methods=["GET", "POST"])
def contact():
    if request.method == "POST":
        name = request.form.get("name")
        email = request.form.get("email")
        msg = request.form.get("message")
        if not name or not email or not msg :
            flash("failed")
            return render_template("contact.html")
        subject = "from  %s" % name
        message = Message(
                  sender="afnanjk2017@gmail.com",
                  recipients=["afnanjk2017@gmail.com"],
                  html="<h2>%s</h2><hr>" % msg + "<p>By: %s <p>" % email, subject=subject)
        mail.send(message)
        flash("Sent!")
        return render_template("contact.html")
    else:
        return render_template("contact.html")






