from django import  forms
from django.forms import ModelForm

#

from .models import *

class CreateTask(forms.ModelForm):
    Title = forms.CharField(widget= forms.TextInput(attrs={'placeholder':'Agregar Tarea...'}))

    class Meta:
        model = Task
        fields = '__all__'