from .models import TimesModel



def get_context(request):
    all_times = []

    times = TimesModel.objects.all()

    for time in times:
        time_info = {
            'user_name': time.user_name,
            'in_time': time.in_time,
            'out_time': time.out_time,
            'in_date': time.in_date,
            'out_date': time.out_date,
            }
        all_times.append(time_info)

    return all_times
    