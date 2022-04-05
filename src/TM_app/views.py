from django.shortcuts import render, redirect
from .forms import TimesForm
from .models import TimesModel
# from django.contrib.auth.urls

# def times_list(request):
#     data = TimesForm.objects.all()
#     return render(request, 'TM_app/times.html', data)


def create(request):
    if request.method == "POST":
        form = TimesForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('create_times')
    else:
        form = TimesForm()

    form = TimesForm()

    all_times = []
    times = TimesModel.objects.all()
    for time in times:
        time_info = {
            'user_name': time.user_name,
            'in_time': time.in_time,
            'out_time': time.out_time,
            'date': time.date
            }
        all_times.append(time_info)
        
    data = {
        'form': form,
        'times': all_times
    }

    return render(request, 'TM_app/times.html', data)
