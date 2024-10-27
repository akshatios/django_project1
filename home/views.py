from django.shortcuts import render , redirect

# Create your views here.
from django.http import HttpResponse
from vege.seed import *
from .utils import send_email_to_client

def send_mail(request):
        send_email_to_client()  # Attempt to send the email
        return redirect('/')  # Redirect to the home page after sending


def home(request):
    seed_db(100)
    
    
    peoples = [
        {'name':"abhijeet gupt",'age':24},
        {'name':"abhit gupt",'age':23},
        {'name':"jeet gupt",'age':17},
        {'name':"bhyt gupt",'age':21}
    ]
    
    for people in peoples:
        if people['age']:
            print(people)
    
    vegetables = ['Pumpkin','Tomato','Potato']
    
    return render(request, "home/index.html",context={'page':'django learning','peoples':peoples,'vegetables':vegetables})
    
    
    
def about(request):
    context = {'page': 'About'}
    return render(request, "home/about.html",context)

def contact(request):
    context = {'page': 'Contact'}
    return render(request, "home/contact.html",context)


def success_page(request):
    print("*" * 10)
    context = {'page': ''}
    return HttpResponse("this is succeess page")