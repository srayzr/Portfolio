# portfolio_app/forms.py
from django import forms
from .models import Programmer, Project

class ProgrammerForm(forms.ModelForm):
    class Meta:
        model = Programmer
        fields = ['user', 'age', 'language', 'framework', 'experience']

class ProjectForm(forms.ModelForm):
    class Meta:
        model = Project
        fields = ['name', 'description']
