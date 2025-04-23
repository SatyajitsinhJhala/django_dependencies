from django.shortcuts import render
from .models import Works, Lives
from .forms import WorksForm, CompanySearchForm

def index(request):
    return render(request, 'company_app/index.html')

def insert_works(request):
    msg = ''
    if request.method == 'POST':
        form = WorksForm(request.POST)
        if form.is_valid():
            person = form.cleaned_data['person_name']
            company = form.cleaned_data['company_name']
            salary = form.cleaned_data['salary']
            street = form.cleaned_data['street']
            city = form.cleaned_data['city']

            # Insert into WORKS
            Works.objects.create(
                person_name=person,
                company_name=company,
                salary=salary
            )

            # Insert into LIVES (overwrite if already exists)
            Lives.objects.update_or_create(
                person_name=person,
                defaults={'street': street, 'city': city}
            )

            msg = 'Entry Added!'
    else:
        form = WorksForm()
    return render(request, 'company_app/insert_works.html', {'form': form, 'message': msg})


def retrieve_people(request):
    msg = ""
    results = []

    if request.method == 'POST':
        form = CompanySearchForm(request.POST)
        if form.is_valid():
            company = form.cleaned_data['company_name']
            works = Works.objects.filter(company_name=company)

            if not works:
                msg = "No records found."
            else:
                for entry in works:
                    try:
                        city = Lives.objects.get(person_name=entry.person_name).city
                    except Lives.DoesNotExist:
                        city = "Unknown"
                    results.append((entry.person_name, city))  # this is a tuple

    else:
        form = CompanySearchForm()

    return render(request, 'company_app/retrieve_people.html', {
        'form': form,
        'results': results,
        'message': msg
    })