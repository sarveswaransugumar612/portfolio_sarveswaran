from django.contrib import admin
from .models import *
# Register your models here.

admin.site.register(Home_clas)
admin.site.register(social_media_clas)
admin.site.register(resume_clas)
admin.site.register(about_yourself_clas)
admin.site.register(skill_clas)
admin.site.register(education_clas)
admin.site.register(certification)
admin.site.register(professional_experince)
admin.site.register(contact_detail)
admin.site.register(contact_form)

class Projectimage(admin.TabularInline):
    model = projectimagefield
class Projectadmin(admin.ModelAdmin):
    inlines = [Projectimage]

admin.site.register(project_detail,Projectadmin)
