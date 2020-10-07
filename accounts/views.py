from django.shortcuts import render, redirect

from .forms import SignUpForm
from .models import Profile

# Create your views here.


def signup(request):
    if request.method == 'POST':
        form = SignUpForm(request.POST)
        address = form.data['address']

        if form.is_valid():
            user = form.save()

            profile = Profile(user=user, address=address)
            profile.save()
            return redirect('login')
    else:
        form = SignUpForm()

    return render(request, 'registration/signup.html', {'form': form})
