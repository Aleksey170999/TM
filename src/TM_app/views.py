from django.shortcuts import render, redirect
from .forms import TimesForm

from . import services


def create(request):
    if request.method == "POST":
        form = TimesForm(request.POST)
        if form.is_valid():
            new_post = form.save(commit=False)
            new_post.user_name = request.user
            new_post.save()            
            
            return redirect('create_times')
        else:
            form = TimesForm()

    form = TimesForm()

    data = {
        'form': form,
        'times': services.get_context(request)
    }

    return render(request, 'TM_app/times.html', data)
