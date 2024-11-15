from django.core.mail import EmailMessage
from core.models import User, OnetimePasscode
from django.conf import settings
import random


def generateOtp():
    otp = ""
    for i in range(6):
        otp += str(random.randint(1, 9))
    return otp


def send_otp_code(email):
    subject = "Votre code de vérification"
    otp_code = generateOtp()
    
    user = User.objects.get(email=email)
    current_site = "schoolbridge-mali.com"
    email_body = f"Salut ! {user.first_name} {user.last_name}, merci pour votre inscription chez {current_site}. Veuillez vérifié votre email \n Code de vérification: {otp_code}"
    from_email = settings.EMAIL_HOST_USER

    OnetimePasscode.objects.create(user=user, code=otp_code)

    s_email = EmailMessage(subject=subject, body=email_body, from_email=from_email, to=[email])
    s_email.send(fail_silently=True )