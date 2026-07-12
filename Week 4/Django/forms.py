from django import forms

class StudentForm(forms.Form):

    name=forms.CharField()

    age=forms.IntegerField()

    email=forms.EmailField()