from django.shortcuts import render
from .models import Works, Lives

def index(request):
    return render(request, 'workapp/index.html')

def insert_data(request):
    if request.method == 'POST':
        person = request.POST['person']
        company = request.POST['company']
        salary = request.POST['salary']
        Works.objects.create(person_name=person, company_name=company, salary=salary)
    return render(request, 'workapp/insert.html')

def query_company(request):
    query = request.GET.get('q')  
    results = Works.objects.filter(name__icontains=query) 
    return render(request, 'workapp/query.html', {'results': results})
