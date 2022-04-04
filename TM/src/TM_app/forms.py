from django.forms import ModelForm, DateTimeInput, DateTimeInput
from .models import TimesModel


class TimesForm(ModelForm):
    class Meta:
        model = TimesModel
        fields = ['user_name', 'in_time', 'out_time']

        widgets = {
            "in_time": DateTimeInput(format="%d %b %Y %H:%M:%S",
                                     attrs={'class': 'form-control',
                                            'placeholder': 'Пришёл'
                                            }),
            "out_time": DateTimeInput(format="%d %b %Y %H:%M:%S",
                                      attrs={
                                          'class': 'form-control',
                                          'placeholder': 'Ушёл'

                                      }),
        }
