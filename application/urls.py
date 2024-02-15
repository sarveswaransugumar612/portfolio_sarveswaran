from django.urls import path
from . import views

urlpatterns = [
    path('',views.home_page,name='home'),
    path('projectdetails/<str:projectname>', views.working_projects_details, name='projectdetails')
]