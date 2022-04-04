from django.shortcuts import render, redirect
from .forms import TimesForm


# def times_list(request):
#     data = TimesForm.objects.all()
#     return render(request, 'TM_app/times.html', data)


def create(request):
    if request.method == "POST":
        form = TimesForm(request.POST)
        if form.is_valid():
            form.save()
    else:
        form = TimesForm()

    form = TimesForm()

    data = {
        'form': form
    }

    return render(request, 'TM_app/times.html', data)
