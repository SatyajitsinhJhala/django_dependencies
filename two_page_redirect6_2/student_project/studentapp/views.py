from django.shortcuts import render, redirect

def first_page(request):
    if request.method == 'POST':
        request.session['name'] = request.POST.get('name')
        request.session['roll'] = request.POST.get('roll')
        request.session['subject'] = request.POST.get('subject')
        return redirect('second-page')
    return render(request, 'studentapp/firstPage.html')

def second_page(request):
    context = {
        'name': request.session.get('name', 'N/A'),
        'roll': request.session.get('roll', 'N/A'),
        'subject': request.session.get('subject', 'N/A'),
    }
    return render(request, 'studentapp/secondPage.html', context)
