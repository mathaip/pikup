from django.shortcuts import render

from django.http import HttpResponse
from django.conf.urls import url,include
from django.contrib.auth import login



def login(request):
    login(request, user)
    return render(request, "registration/registration_form.html")
    
#################################################################################################################################################################################
#LOGIN PAGE VIEW FUNCTION
#################################################################################################################################################################################

#LOGOUT Page View Function!
def logout(request):
    return render(request, 'registration/registration_form.html')

    
#################################################################################################################################################################################
#LOGIN PAGE VIEW FUNCTION
#################################################################################################################################################################################

#LOGIN Page View Function!

    
#################################################################################################################################################################################
#LANDING PAGE VIEW FUNCTION
#################################################################################################################################################################################

#LANDING Page View Function!
def landing(request):
    return render(request, 'landingpage/land-page.html')
    

#################################################################################################################################################################################
#REGISTRATION PAGE VIEW FUNCTION
#################################################################################################################################################################################

#REGISTRATION Page View Function!
def dregistration(request):
    return render(request, 'landingpage/land-page.html')

def driver(request):
    return render(request, 'driver/home.html')
def dprofile(request):
    return render(request, 'driver/profile.html')

#################################################################################################################################################################################
#VIEW FUNCTION FOR  DRIVER'S  DESTINATION-PAGE
#################################################################################################################################################################################

#DRIVER'S  DESTINATION-PAGE view function

'''
 This page enables driver choose a destination point where they can drop off users and get other destination points
'''
def ddestination(request):
    return render(request, 'driver/destination.html')

#################################################################################################################################################################################
#VIEW FUNCTION FOR  DRIVER'S  CONTACT-PAGE
#################################################################################################################################################################################

#DRIVER'S  DESTINATION-PAGE view function

'''
 This page gives driver contact info
'''
def dcontact(request):
    return render(request, 'driver/contact.html')

#################################################################################################################################################################################
#VIEW FUNCTION FOR  ABOUT-PAGE
#################################################################################################################################################################################

#ABOUT-INFO-PAGE

'''
 This page basically explains what the app is about
'''
def about(request):
    return render(request, 'driver/about.html')

#################################################################################################################################################################################s

#################################################################################################################################################################################
#VIEW FUNCTION FOR  DRIVER'S HOME-PAGE
#################################################################################################################################################################################

#Driver's HOME-PAGE view function