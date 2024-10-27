from home.models import student
import time
from django.core.mail import send_mail
from django.conf import settings


def run_this_function():
    print("Function Started")    
    
    
    time.sleep(1)
    print("Functin Executed")
    
    
    
def send_email_to_client():
    subject = "this email is from django server"
    message = "this is the texxt message from djang server"
    from_email = settings.EMAIL_HOST_USER
    recipient_list = ["akshatjain9989@gmail.com"]
    
    
    send_mail(subject, message, from_email , recipient_list )
    