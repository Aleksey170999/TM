from django.forms import ModelForm, DateTimeInput, TextInput
from django import forms
from .models import TimesModel


class DateInput(forms.DateInput):
    input_type = 'date'
    

class TimeInput(forms.TimeInput):
    input_type = 'time'


class TimesForm(ModelForm):
    class Meta:
        model = TimesModel
        fields = ['user_name', 'date', 'in_time', 'out_time']

        widgets = {
            'date': DateInput(attrs={'class': 'form-control',
                                     'placeholder': 'Дата'
                                    }),
                                        
            "in_time": TimeInput(attrs={'class': 'form-control',
                                        'placeholder': 'Пришёл'
                                        }),

            "out_time": TimeInput(attrs={'class': 'form-control',
                                         'placeholder': 'Ушёл'
                                         }),

            "user_name": TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'Ушёл'
            }),
        }
