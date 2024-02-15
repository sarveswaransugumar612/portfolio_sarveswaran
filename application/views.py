from django.shortcuts import render, redirect
from .models import *
from django.contrib import messages
from django.conf import settings
from django.core.mail import send_mail
from django.template.loader import render_to_string


# Create your views here

def home_page(request):
    if request.method == 'POST':
        name = request.POST['name']
        email = request.POST['email']
        subject = request.POST['subject']
        message = request.POST['message']
        html = render_to_string('mailtemplate.html', {
            'getname': name,
            'getemail': email,
            'getsubject': subject,
            'getmessage': message
        })
        send_mail('Contact Form', "subject", settings.EMAIL_HOST_USER, ["sarveswaran612@gmail.com"], html_message=html)

        contactformdata = contact_form(name=name, email=email, subject=subject, message=message)
        contactformdata.save()

        messages.success(request, "Your Message has been Submitted Successfully")
        # return redirect('#')

    homeobjects = Home_clas.objects.all()
    socialmediaobjects = social_media_clas.objects.all()
    aboutusobjects = about_yourself_clas.objects.all()
    skillsobjects = skill_clas.objects.all()
    education_objects = education_clas.objects.all()
    certificate_objects = certification.objects.all()
    professional_experince_objects = professional_experince.objects.all()
    working_project_objects = project_detail.objects.all()
    contact_objects = contact_detail.objects.all()

    return render(request, 'index.html', {
        'home': homeobjects,
        'socialmedias':socialmediaobjects,
        'aboutus': aboutusobjects,
        'skills': skillsobjects,
        'education': education_objects,
        'certificate': certificate_objects,
        'professionalexperince': professional_experince_objects,
        'workingproject': working_project_objects,
        'contactdetails': contact_objects,
    })


def working_projects_details(request, projectname):
    projects_details_objects = project_detail.objects.filter(project_name=projectname)
    projectimagefield_objects = projectimagefield.objects.all()
    print(projectimagefield_objects)
    return render(request, 'projectdetails.html', {
        'projectdetails': projects_details_objects,
        'projectimages':projectimagefield_objects
    })
