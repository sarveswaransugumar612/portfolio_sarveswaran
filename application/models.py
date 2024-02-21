from django.db import models
from ckeditor.fields import RichTextField

# Create your models here.

class Home_clas(models.Model):
    title = models.CharField(max_length=30)
    name = models.CharField(max_length=50)
    role = models.CharField(max_length=100)
    back_ground_image = models.ImageField(upload_to='mainbackground/')

    def __str__(self):
        return  self.name

class social_media_clas(models.Model):
    social_media_type = models.CharField(help_text="Ex : linkedin", max_length=40)
    social_media_link = models.CharField(max_length=200)

    def __str__(self):
        return self.social_media_type

class resume_clas(models.Model):
    resume_title = models.CharField(max_length = 100)
    resume_file = models.FileField(upload_to='resumefile/')

    def __str__(self):
        return self.resume_title

class about_yourself_clas(models.Model):
    about_yourself = models.CharField(max_length=500)
    profile_image = models.ImageField(upload_to='profile/')
    date_of_birth = models.CharField(max_length=20,help_text="Ex : 1 Jan 2001 ")
    email = models.CharField(max_length=40)
    phone = models.CharField(max_length=13)
    degree = models.CharField(max_length=10)
    city = models.CharField(max_length=30)
    age = models.CharField(max_length=2)
    website = models.CharField(max_length=100)
    years_of_experience = models.CharField(max_length=30,help_text='Ex : 1 year 7 months')

    def __str__(self):
        return  self.email

class skill_clas(models.Model):
    skill_name = models.CharField(max_length=30)
    percentage = models.CharField(max_length=3)

    def __str__(self):
        return  self.skill_name

class education_clas(models.Model):
    degree_name = models.CharField(max_length=50)
    duration = models.CharField(max_length=20)
    college_name = models.CharField(max_length=100)

    def __str__(self):
        return self.degree_name

class certification(models.Model):
    certificate_name = models.CharField(max_length=50)
    duration = models.CharField(max_length=20)
    center_name = models.CharField(max_length=100)

    def __str__(self):
        return self.certificate_name

class professional_experince(models.Model):
    professional_experince_title = models.CharField(max_length=100)
    professional_experince_duration = models.CharField(max_length=20)
    professional_experince_detail = RichTextField()

    def __str__(self):
        return self.professional_experince_title

class project_detail(models.Model):
    categoryname = models.CharField(max_length=20, help_text="Ex : app or web")
    project_image = models.ImageField(upload_to='projects/')
    project_name = models.CharField(max_length=50)
    project_overview = RichTextField()
    projectcategory = models.CharField(max_length=20, help_text="Ex : Application or Website")
    clientname = models.CharField(max_length=20)
    projectduration = models.CharField(max_length=20, help_text="Ex : Nov 2021 - Jun 2022")
    projecturl = models.CharField(max_length=200)

    def __str__(self):
        return self.project_name

class projectimagefield(models.Model):
    name = models.ForeignKey(project_detail,on_delete=models.CASCADE)
    projectimg = models.ImageField(upload_to='projectimg/')

    def __int__(self):
        return self.name

class contact_detail(models.Model):
    address = models.CharField(max_length=100)
    phone = models.CharField(max_length=15)
    email = models.EmailField(max_length=30)

    def __str__(self):
        return self.phone

class contact_form(models.Model):
    name = models.CharField(max_length=30)
    email = models.EmailField(max_length=30)
    subject = models.CharField(max_length=30)
    message = models.CharField(max_length=500)

    def __str__(self):
        return self.name