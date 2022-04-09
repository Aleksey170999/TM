from django.forms import ModelForm, TextInput
from django import forms
from .models import TimesModel

class DateInput(forms.DateInput):
    input_type = 'date'
    

class TimeInput(forms.TimeInput):
    input_type = 'time'


class TimesForm(ModelForm):
    class Meta:
        model = TimesModel

        exclude = ["user_name"]


        widgets = {            
            'in_date': DateInput(attrs={'class': 'form-control'}),

            'out_date': DateInput(attrs={'class': 'form-control'}),
                                        
            "in_time": TimeInput(attrs={'class': 'form-control'}),

            "out_time": TimeInput(attrs={'class': 'form-control'}),
        }
