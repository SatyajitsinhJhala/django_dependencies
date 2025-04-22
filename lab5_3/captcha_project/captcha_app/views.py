from django.shortcuts import render
from .forms import CaptchaForm

# Use a fixed CAPTCHA value
CAPTCHA_TEXT = "AB12C"

def captcha_view(request):
    form = CaptchaForm()
    message = ""
    disable_input = False

    if 'attempts' not in request.session:
        request.session['attempts'] = 0

    if request.method == 'POST':
        form = CaptchaForm(request.POST)
        if form.is_valid():
            user_input = form.cleaned_data['captcha_input']
            if user_input == CAPTCHA_TEXT:
                message = "✅ CAPTCHA Matched!"
                request.session['attempts'] = 0  # Reset on success
            else:
                request.session['attempts'] += 1
                if request.session['attempts'] >= 3:
                    message = "❌ Too many failed attempts. Try later."
                    disable_input = True
                else:
                    message = f"❌ CAPTCHA Mismatch. Attempts left: {3 - request.session['attempts']}"

    return render(request, 'captcha_app/captcha.html', {
        'form': form,
        'captcha_text': CAPTCHA_TEXT,
        'message': message,
        'disable_input': disable_input
    })
