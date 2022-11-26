from django.shortcuts import render, redirect
from Student.Student_Insert_Form import StudentForm
from Student.models import Student, StudentMarks


# Create your views here.
def index(request):
    return render(request, "index.html")

def home(request):
    data=Student.objects.all()
    return render(request, "index.html", {'student':data})

def Student_Delete(request, id):
    student = Student.objects.get(id=id)
    student.delete()
    return redirect("/Home")

def Student_Insert(request):
    form = StudentForm()
    if request.method == "POST":
        form = StudentForm(request.POST)
        if form.is_valid:
            form.save()
            return redirect("/Home")
    return render(request, 'Create.html', {'form':form})

def Student_Update(request, id):
    student = Student.objects.get(id=id)
    if request.method == "POST":
        form = StudentForm(request.POST, instance=student)
        if form.is_valid:
            form.save()
            return redirect("/Home")
    return render(request, 'Update.html', {'student':student})

def about(request):
    data2=StudentMarks.objects.all()
    return render(request, "About.html", {'marks':data2})
    
def contact(request):
    return render(request, "Head.html")

