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
        fields = ['user_name', 'in_date', 'out_date', 'in_time', 'out_time']

        widgets = {
            'user_name': TextInput(attrs={'class': 'form-control'}),  
            
            'in_date': DateInput(attrs={'class': 'form-control'}),

            'out_date': DateInput(attrs={'class': 'form-control'}),
                                        
            "in_time": TimeInput(attrs={'class': 'form-control'}),

            "out_time": TimeInput(attrs={'class': 'form-control'}),
        }
