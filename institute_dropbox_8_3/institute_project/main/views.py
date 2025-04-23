from django.shortcuts import render, redirect
from .models import Institute
from .forms import InstituteForm

def select_institute(request):
    if request.method == "POST":
        form = InstituteForm(request.POST)
        if form.is_valid():
            selected_id = form.cleaned_data['institute'].id
            return redirect('institute_details', institute_id=selected_id)
    else:
        form = InstituteForm()
    return render(request, 'select_institute.html', {'form': form})

def institute_details(request, institute_id):
    institute = Institute.objects.get(id=institute_id)
    return render(request, 'institute_details.html', {'institute': institute})
