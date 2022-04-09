from django.shortcuts import render, redirect
from .forms import TimesForm

from . import services


def create(request):
    if request.method == "POST":
        form = TimesForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('create_times')
        else:
            form = TimesForm()

    form = TimesForm()

    data = {
        'form': form,
        'times': services.get_context(request)
    }

    return render(request, 'TM_app/times.html', data)
