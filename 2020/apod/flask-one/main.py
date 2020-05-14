from flask import Flask, render_template, url_for, flash, redirect
from buttons import emailButton

import smtplib, ssl
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
from email.mime.image import MIMEImage

####### Getting NASA APOD Image ########
import requests, urllib, json, os

key = # < your api key here > 
url = "https://api.nasa.gov/planetary/apod?api_key={}".format(key)
file = requests.get(url)
file.raise_for_status()
urllib.request.urlretrieve(json.loads(file.text)['url'], "nasaapodsample.jpg")
########################################

app = Flask(__name__)
app.config['SECRET_KEY'] = '52eb1d1cd0267b75c13000225d0b39b2' #secrets.token_hex(16)

def send_email(sendTo):
    smtp_server =  'smtp.gmail.com'
    port = 587
    sender_email = "mehulpy@gmail.com"
    receiver_email = sendTo
    password = # enter your password

    # using MIME for stylised emails
    message = MIMEMultipart("alternative")
    message['Subject'] = 'Style Test I'
    message['From'] = sender_email
    message['To'] = receiver_email

    # plain text message
    text = """\
    It's day 21, ... no ... day 22 \n
    Food and water ran out 4 days ago \n
    Oxygen runs out tomorrow morning,  and that'll be it \n
    please know that I will dream about you, because it's always you \n
    """

    # HTML message
    html = """\
    <html>
      <body>
        <p>
        Hi, how are you? <br>
        I hope this email finds you well <br>
        I was hoping you could check out this <a href="https://www.space.com/28973-best-space-books.html" target="_blank">website</a> and tell me if using it is worthwhile
        </p>
      </body>
    </html>
    """

    # turn into MIME objects
    part1 = MIMEText(text, "plain")
    part2 = MIMEText(html, "html")
    message.attach(part1)
    message.attach(part2)

    # attaching our sample image
    img_data = open("nasaapodsample.jpg", 'rb').read()
    image = MIMEImage(img_data, name=os.path.basename("nasaapodsample.jpg"))
    message.attach(image)


    # create secure SSL context
    context = ssl.create_default_context()

    # log in and send sender_email
    try:
        server = smtplib.SMTP(smtp_server, port)
        server.ehlo()
        server.starttls(context=context)
        server.ehlo()
        server.login(sender_email, password)
        server.sendmail(sender_email, receiver_email, message.as_string())
    except Exception as e:
        print(e)
    finally:
        server.quit()

@app.route('/', methods=['POST', 'GET'])
def home():
    form = emailButton()
    if form.validate_on_submit():
        send_email(form.email.data)
        return redirect(url_for('bye'))
    return render_template('home.html', form=form)


@app.route('/bye')
def bye():
    return render_template('bye.html')
