from django.shortcuts import render
from django.shortcuts import render, redirect
from django.shortcuts import render, redirect, get_object_or_404
from .forms import StudentForm
from .models import Student

def student_profile(request):
    form = StudentForm()
    success = False  # Flag for success
    if request.method == 'POST':
        form = StudentForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()  # Save to database
            success = True  # Set success flag
            form = StudentForm()  # Reset the form
    return render(request, 'index.html', {'form': form, 'success': success})


from django.shortcuts import render
from .models import Student  # Assuming you have a Student model

def view_students(request):
    students = Student.objects.all()  # Fetch all student records from the database
    return render(request, 'view.html', {'students': students})



from django.shortcuts import render, get_object_or_404, redirect
from django.contrib import messages

def delete_student(request, student_id):
    student = get_object_or_404(Student, student_id=student_id)
    if request.method == "POST":
        student.delete()
        messages.success(request, "Student profile deleted")
        return redirect('view_students')


# Edit Student
def edit_student(request, student_id):
    student = get_object_or_404(Student, student_id=student_id)
    if request.method == "POST":
        form = StudentForm(request.POST, request.FILES, instance=student)
        if form.is_valid():
            form.save()
            return redirect('view_students')  # Redirect to the student list page
    else:
        form = StudentForm(instance=student)
    return render(request, 'edit_student.html', {'form': form, 'student': student})



def index(request):
    return render(request, 'index.html')