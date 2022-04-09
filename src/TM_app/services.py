from datetime import datetime
from .models import TimesModel



def get_context(request):
    all_times = []

    times = TimesModel.objects.all()

    for time in times:
        year_in = int(str(time.in_date).split('-')[0])
        month_in = int(str(time.in_date).split('-')[1])
        day_in = int(str(time.in_date).split('-')[2])
        hour_in = int(str(time.in_time).split(':')[0])
        minutes_in = int(str(time.in_time).split(':')[1])

        year_out = int(str(time.out_date).split('-')[0])
        month_out = int(str(time.out_date).split('-')[1])
        day_out = int(str(time.out_date).split('-')[2])
        hour_out = int(str(time.out_time).split(':')[0])
        minutes_out = int(str(time.out_time).split(':')[1])

        dt_in = datetime(year=year_in, month=month_in, day=day_in, hour=hour_in, minute=minutes_in, second=0)
        dt_out = datetime(year=year_out, month=month_out, day=day_out, hour=hour_out, minute=minutes_out, second=0)

        pere = dt_out - dt_in

        time_info = {
            'user_name': request.user.username,
            'in_time': time.in_time,
            'out_time': time.out_time,
            'in_date': time.in_date,
            'out_date': time.out_date,
            'pere': pere
            }
        all_times.append(time_info)

    return all_times
    