from django.forms import ModelForm, DateTimeInput, TextInput
from django import forms
from django.http import request
from .models import TimesModel

class DateInput(forms.DateInput):
    input_type = 'date'
    

class TimeInput(forms.TimeInput):
    input_type = 'time'


class TimesForm(ModelForm):
    class Meta:
        model = TimesModel
        fields = ['user_name','in_date', 'out_date', 'in_time', 'out_time', 'pere']

        widgets = {
            'user_name': TextInput(attrs={'class': 'form-control',
                            'placeholder': 'Имя',
                            'id': 'InputDate',
                        }),
            'in_date': DateInput(attrs={'class': 'form-control',
                                     'placeholder': 'Дата прихода',
                                     'id': 'InputDate',
                                    }),
            'out_date': DateInput(attrs={'class': 'form-control',
                                     'placeholder': 'Дата ухода',
                                     'id': 'InputDate',
                                    }),
                                        
            "in_time": TimeInput(attrs={'class': 'form-control',
                                        'placeholder': 'Пришёл',
                                        'id': 'InputInTime',
                                        }),

            "out_time": TimeInput(attrs={'class': 'form-control',
                                         'placeholder': 'Ушёл',
                                         'id': 'InputOutTime',
                                         }),
            'user_name': TextInput(attrs={'class': 'form-control',
                                         'placeholder': 'Имя',
                                         'id': 'InputDate',
                                         }),
        }
