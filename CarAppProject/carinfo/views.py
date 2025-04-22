from django.shortcuts import render

def index(request):
    manufacturers = ['Toyota', 'Ford', 'Honda', 'BMW', 'Tesla']
    return render(request, 'index.html', {'manufacturers': manufacturers})

def result(request):
    manufacturer = request.GET.get('manufacturer')
    model = request.GET.get('model')
    return render(request, 'result.html', {'manufacturer': manufacturer, 'model': model})
