from django.shortcuts import render
from django.shortcuts import render, redirect
from django.shortcuts import render, redirect, get_object_or_404
from .forms import StudentForm
from .models import Student
from django.db.models import Q


from django.contrib import messages  # For displaying alert messages


from django.shortcuts import render
from django.http import JsonResponse
from .forms import StudentForm
from .models import Student  # Assuming you have a Student model

def student_profile(request):
    form = StudentForm()
    success = False  # Flag for success
    alert_message = ""  # Initialize an alert message

    if request.method == 'POST':
        student_id = request.POST.get('student_id')
       

        # Check if a student with the same ID and name already exists
        if Student.objects.filter(student_id=student_id).exists():
            alert_message = "Student already exists!"  # Set the alert message
        else:
            form = StudentForm(request.POST, request.FILES)
            if form.is_valid(): 
                form.save()  # Save to database
                success = True  # Set success flag
                alert_message = "Student profile registered successfully!"
                form = StudentForm()  # Reset the form

    return render(request, 'index.html', {'form': form, 'success': success, 'alert_message': alert_message})




from django.shortcuts import render
from .models import Student  # Assuming you have a Student model

from django.shortcuts import render
from django.db.models import Q
from .models import Student

def view_students(request):
    # Get the search query from the URL
    search_query = request.GET.get('search', '')  # Get 'search' parameter from the GET request

    if search_query:
        # If a search query is provided, filter by ID or Name (case-insensitive)
        students = Student.objects.filter(
            Q(student_id__icontains=search_query) | Q(name__icontains=search_query)
        )
    else:
        # If no search query, fetch all student records
        students = Student.objects.all()
    
    return render(request, 'view.html', {'students': students, 'search_query': search_query})



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



def view_student_details(request, student_id):
    student = get_object_or_404(Student, student_id=student_id)
    return render(request, 'student_details.html', {'student': student})