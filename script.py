import smtplib
from email.message import EmailMessage

# All emails
emails = [
    "praveen.singh@xduce.com",
    "praveen.zore@agiliad.com",
    "pravin.kankane@flo-group.com",
    "pravin.subba@tanla.com",
    "preeth.joseph@bridgei2i.com",
    "preetha@frontier.in",
    "preetham.singh@tanla.com",
    "preethy.paul@insemitech.com",
    "preeti.das@tripstack.com",
    "preeti.kalyankar@mosambee.com",
    "pmani@verisys.com",
    "preeti.mathur@eproductivitysoftware.com",
    "preeti.msw@wundermanthompson.com",
    "preeti.phansalkar@clariontech.com",
    "preety@cozentus.com",
    "prem.nair@toshiba-tsip.com",
    "prerna.kohli@cyware.com",
    "prince.kumar@innohubtechnologies.com",
    "priscilla.f@mantralabsglobal.com",
    "pritha@near.com",
    "priti.mhatre@zaggle.in",
    "priya.bagla@fullestop.com",
    "priya.bhogineni@yexle.com",
    "priya.malhotra@daffodilsw.com",
    "priya@flexasoft.com",
    "priya@congruentindia.com"
]

# Email Content
SUBJECT = "Application for Software Developer / Full Stack Developer Role"
BODY = """
Dear Hiring Team,

I hope you are doing well. My name is Bharat Sharma, and I am writing to apply for the Software Developer / Full Stack Developer position.

I have hands-on experience in MERN Stack, Laravel, JavaScript, JWT Authentication, Payment Integration, API Development, and backend systems. I have worked on real-world projects including finance management systems, automation modules, and secure authentication systems.

I am confident that my skills and practical development experience make me a strong fit for your engineering team.

Kindly find my resume attached. I would appreciate the opportunity to discuss how I can contribute.

Thank you for your time.

Regards,
Bharat Sharma  
Portfolio: https://www.devfolio.cc/bhar1gitr
GitHub: https://github.com/bhar1gitr  
LinkedIn: https://www.linkedin.com/in/bharat-sharma-50208b238/
"""

# SMTP Settings
SENDER_EMAIL = "bharatsharma98971@gmail.com"
APP_PASSWORD = "hggd byhq gzup wxnj"

# Resume Path (uploaded file)
RESUME_PATH = "./Resume_Bharat Sharma.pdf"

def send_mail(to_email):
    msg = EmailMessage()
    msg["From"] = SENDER_EMAIL
    msg["To"] = to_email
    msg["Subject"] = SUBJECT
    msg.set_content(BODY)

    # Attach resume
    with open(RESUME_PATH, "rb") as f:
        file_data = f.read()
        msg.add_attachment(file_data, maintype="application", subtype="pdf", filename="Bharat_Resume.pdf")

    # Send Email
    with smtplib.SMTP_SSL("smtp.gmail.com", 465) as smtp:
        smtp.login(SENDER_EMAIL, APP_PASSWORD)
        smtp.send_message(msg)

    print(f"Email sent to: {to_email}")


# Send email to all
for email in emails:
    send_mail(email)

print("All emails sent successfully!")
