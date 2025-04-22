from django.shortcuts import render
from .forms import PromotionCheckForm
from datetime import date

def check_promotion(request):
    result = ""
    if request.method == 'POST':
        form = PromotionCheckForm(request.POST)
        if form.is_valid():
            doj = form.cleaned_data['date_of_joining']
            experience = (date.today() - doj).days / 365.25
            result = "YES" if experience >= 5 else "NO"
    else:
        form = PromotionCheckForm()

    return render(request, 'promotion/check.html', {'form': form, 'result': result})
