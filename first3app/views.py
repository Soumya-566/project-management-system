from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.
from django.contrib import messages
from first3app.models import Student,Faculty,Admin
def faculty(request):
	if request.method=="POST":
		uname=request.POST['facultyname']
		rno=request.POST['password']
		try:
			data=Faculty.objects.get(username=uname,password=rno)
			if data:
				return render(request,'first3app/f1.html',{'o':data})
		except Exception:
			messages.warning(request,'Please enter valid details!!!.......')
			return render(request,'first3app/faculty.html')

	return render(request,'first3app/faculty.html')
def adminlogin(request):
	if request.method=="POST":
		u=request.POST['username']
		p=request.POST['password']
		try:
			data=Admin.objects.get(username=u)
			if data:
				return render(request,'first3app/a1.html')
		except:
			messages.warning(request,'Please enter valid details!!!.......')
			return render(request,'first3app/adminlogin.html')			

	return render(request,'first3app/adminlogin.html')
def student(request):
	if request.method=="POST":
		uname=request.POST['username']
		rno=request.POST['password']
		
		
		try:
			data=Student.objects.get(username=uname,password=rno)
			return render(request,'first3app/s1.html',{'o':data})
			
		except Exception:
					messages.warning(request,'Please enter valid details!!!.......')
					return render(request,'first3app/students.html')
	return render(request,'first3app/students.html')
def facultydetails(request):
	o=Faculty.objects.all()
	return render(request,'first3app/facultydetails.html',{'o':o})
def projectsinfo(request):
	return render(request,'first3app/projectsinfo.html')
def updateproject(request,name):
	o=Student.objects.get(username=name)
	if request.method=="POST":
		a=request.POST['projectstatus']
		b=request.POST['query']
		c=request.POST['date']
		p=Student.objects.get(username=name)
		if b:
			x=p.query
			Student.objects.filter(username=name).update(query=b)
		Student.objects.filter(username=name).update(projectstatus=a+p.projectstatus)
		Student.objects.filter(username=name).update(date=c)
		#return HttpResponse("successfully updated........!")
		messages.warning(request,'Successfully updated')
		#return render(request,'first3app/home.html')
	return render(request,'first3app/updateproject.html' ,{'o':o})
def facultyfeedback(request,name):
	o=Student.objects.get(username=name)
	return render(request,'first3app/facultyfeedback.html',{'o':o})
def home(request):
	return render(request,'first3app/home.html')
def Projects1519cse1(request):
	return render(request,'first3app/Projects1519cse1.html')
def Projects1519cse2(request):
	return render(request,'first3app/Projects1519cse2.html')
def Projects1620cse1(request):
	return render(request,'first3app/Projects1620cse1.html')
def Projects1620cse2(request):
	return render(request,'first3app/Projects1620cse2.html')

def Projects2020(request):
	o=Student.objects.all()
	return render(request,'first3app/Projects2020.html',{'o':o})
def givefeedback(request,name):
	if request.method=="POST":
		bno=request.POST['bno']
		feedback=request.POST['feedback']
		try:
			o=Student.objects.get(username=bno)
			f=o.feedback
			h=f+""+name+":"+feedback
		
			Student.objects.filter(username=bno).update(feedback=h)
			#return HttpResponse("successfully given")
			messages.warning(request,'Successfully updated')
		except:
			return HttpResponse("Incorrect batch no...!")
	of=Faculty.objects.get(username=name)
	return render(request,'first3app/givefeedback.html',{'of':of})
def adminpasswordreset(request):
	
	if request.method=="POST":
		u=request.POST['u']
		o=request.POST['o']
		n=request.POST['n']
		try:
			p=Admin.objects.get(username=u,password=o)
			Admin.objects.filter(username=u,password=o).update(password=n)
			return HttpResponse("successfully updated......!")
		except:
			messages.warning(request,'Please enter valid details!!!.......')
			return render(request,'first3app/adminpasswordreset.html')
	return render(request,'first3app/adminpasswordreset.html')
def fpasswordreset(request):
	if request.method=="POST":
		u=request.POST['u']
		o=request.POST['o']
		n=request.POST['n']
		try:
			p=Faculty.objects.get(username=u,password=o)
			Faculty.objects.filter(username=u,password=o).update(password=n)
			#return HttpResponse("successfully updated......!")
			messages.warning(request,'Successfully updated')
		except:
			messages.warning(request,'Please enter valid details!!!.......')
			return render(request,'first3app/fpasswordreset.html')
	return render(request,'first3app/fpasswordreset.html')
def spasswordreset(request):
	if request.method=="POST":
		u=request.POST['u']
		o=request.POST['o']
		n=request.POST['n']
		try:
			p=Student.objects.get(username=u,password=o)
			Student.objects.filter(username=u,password=o).update(password=n)
			#return HttpResponse("successfully updated......!")
			messages.warning(request,'Successfully updated')
		except:
			messages.warning(request,'Please enter valid details!!!.......')
			return render(request,'first3app/spasswordreset.html')
	return render(request,'first3app/spasswordreset.html')
def studentsignup(request):
	if request.method=="POST":
		bno=request.POST['username']
		pwd=request.POST['password']
		facultyundertaking=request.POST['fu']
		projectname=request.POST['Project name']
		try:
				Student.objects.create(username=bno,password=pwd,nameoffaculty=facultyundertaking,projectname=projectname)
				data=Student.objects.get(username=bno)
				return render(request,'first3app/s1.html',{'o':data})
		except Exception:
				#return HttpResponse("Account Already exists try logging in!")
				messages.warning(request,'User already exists try logging in!!!.......')
				return render(request,'first3app/studentssignup.html')
	return render(request,"first3app/studentsignup.html")
def facultysignup(request):
	if request.method=="POST":
		fn=request.POST['fn']
		pwd=request.POST['pwd']
		try:
			Faculty.objects.create(username=fn,password=pwd)
			s=Faculty.objects.get(username=fn)
			return render(request,'first3app/f1.html',{'o':s})
		except:
			return HttpResponse("user already exists try logging in........!")
			#messages.warning(request,'user already exists try logging in........!')
			#return render(request,'first3app/spasswordreset.html')
	return render(request,'first3app/facultysignup.html')
def s1(request):
	return render(request,'first3app/s1.html')
def addadmin(request):
	if request.method=="POST":
		un=request.POST['un']		
		pwd=request.POST['pwd']
		try:
			Admin.objects.create(username=un,password=pwd)
			messages.warning(request,'account succssfully created........!')
			#return HttpResponse("successfully account created.......!")
		except:
			messages.warning(request,'admin already exists........!')
			#return HttpResponse("admin already exists try logging in........!")
	return render(request,'first3app/addadmin.html')
def removefaculty(request):
	if request.method=="POST":
		a=request.POST['un']
		try:
			Faculty.objects.filter(username=a).delete()
			return HttpResponse("successfully deleted......!")
		except:
			return HttpResponse("incorrect username...!")
		
	return render(request,'first3app/removefaculty.html')
def removestudent(request):
	if request.method=="POST":
		a=request.POST['un']
		try:
			p=Student.objects.get(username=a)
			p.delete()
			return HttpResponse("successfully deleted.......!")
		except:
			return HttpResponse("incorrect details.......!")
	return render(request,'first3app/removestudent.html')
def studentdetails(request):
	o=Student.objects.all()
	return render(request,'first3app/studentdetails.html',{'o':o})
def a1(request):
	return render(request,"first3app/a1.html")