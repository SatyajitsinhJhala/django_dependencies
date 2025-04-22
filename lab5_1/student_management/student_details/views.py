from django.shortcuts import render
from .forms import StudentForm

def student_form(request):
    form = StudentForm()
    student_details = ""
    percentage = None
    
    if request.method == 'POST':
        form = StudentForm(request.POST)
        if form.is_valid():
            student = form.save(commit=False)
            
            # Calculate percentage
            percentage = student.get_percentage()
            
            # Format student details for textarea
            student_details = f"""
Name: {student.name}
Date of Birth: {student.date_of_birth}
Address: {student.address}
Contact Number: {student.contact_number}
Email: {student.email}
Marks:
  English: {student.english_marks}
  Physics: {student.physics_marks}
  Chemistry: {student.chemistry_marks}
Total Percentage: {percentage:.2f}%
"""
    
    return render(request, 'student_details/student_form.html', {
        'form': form,
        'student_details': student_details,
        'percentage': percentage
    })