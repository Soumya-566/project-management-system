"""sample3 URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from first3app import views
urlpatterns = [
    path('admin/', admin.site.urls),
    path('faculty/', views.faculty,name='faculty'),
    path('student/', views.student,name='student'),
    path('home/',views.home,name='home'),
    path('studentsignup/',views.studentsignup,name='studentsignup'),
    path('facultysignup/',views.facultysignup,name='facultysignup'),
    path('s1/',views.s1,name="s1"),
    path('projectsinfo/',views.projectsinfo,name="projectsinfo"),
    path('facultydetails/',views.facultydetails,name="facultydetails"),
    path('updateproject/<str:name>/',views.updateproject,name="updateproject"),
    path('facultyfeedback/<str:name>/',views.facultyfeedback,name="facultyfeedback"),
    path('Projects2020/',views.Projects2020,name="Projects2020"),
    path('givefeedback/<str:name>/',views.givefeedback,name="givefeedback"),
    path('adminlogin/',views.adminlogin,name="adminlogin"),
    path('a1/',views.a1,name="a1"),
    path('studentdetails/',views.studentdetails,name="studentdetails"),
    path('addadmin/',views.addadmin,name="addadmin"),
    path('removestudent/',views.removestudent,name="removestudent"),
    path('removefaculty/',views.removefaculty,name="removefaculty"),
    path('spasswordreset/',views.spasswordreset,name="spasswordreset"),
    path('adminpasswordreset/',views.adminpasswordreset,name="adminpasswordreset"),
    path('fpasswordreset/',views.fpasswordreset,name="fpasswordreset"),
    path('Projects1519cse1/',views.Projects1519cse1,name="Projects1519cse1"),
    path('Projects1519cse2/',views.Projects1519cse2,name="Projects1519cse2"),
    path('Projects1620cse1/',views.Projects1620cse1,name="Projects1620cse1"),
    path('Projects1620cse2/',views.Projects1620cse2,name="Projects1620cse2"),

]
