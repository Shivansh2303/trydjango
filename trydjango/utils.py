from django.core.mail import send_mail

def sendMail(title,message,to_email,html_message=None):
            from_email='noreply@mail.com'
            send_mail(title,message,to_email,from_email,html_template)
    return send_mail
# def sendMassMail()