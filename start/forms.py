from django import forms
from django.contrib.auth.models import User
from django.forms import NumberInput

from .models import *

class AddCandidateForm(forms.Form):
    name = forms.CharField(widget=forms.TextInput(attrs={"class":"form-control", "placeholder":"ФИО"}),required=True)
    phone = forms.CharField(widget=forms.TextInput(attrs={"class":"form-control", "placeholder":"89........."}),required=True)
    email = forms.EmailField(widget=forms.EmailInput(attrs={"class":"form-control", "placeholder":"example@mail.ru"}),required=True)
    sex = forms.CharField(widget=forms.TextInput(attrs={"class":"form-control", "placeholder":"Муж/жен"}),required=True)
    position = forms.CharField(widget=forms.TextInput(attrs={"class":"form-control", "placeholder":"Разработчик"}),required=True)
    photo = forms.ImageField(widget=forms.FileInput(attrs={"class":"form-control", "placeholder":"Фото"}),required=False)
    birthdate = forms.DateField(widget=NumberInput(attrs={'type': 'date', "class":"form-control", "placeholder":"01.01.1999"}),required=True)
    cv = forms.FileField(widget=forms.FileInput(attrs={"class":"form-control"}),required=False)
    class Meta:
        model = Candidate
        fields = ('username', 'phone', 'email', 'sex', 'photo', 'birthdate', 'cv')

class AddJobForm(forms.Form):
    name = forms.CharField(widget=forms.TextInput(attrs={"placeholder":"iOS Developer"}),required=True)
    salary = forms.IntegerField(widget=forms.NumberInput(attrs={"placeholder":"20000"}),required=True)
    expirence = forms.IntegerField(widget=forms.NumberInput(attrs={"placeholder":"1"}),required=True)
    employment = forms.CharField(widget=forms.TextInput(attrs={"placeholder":"Полная/частичная"}),required=True)
    definition = forms.CharField(widget=forms.TextInput(attrs={"placeholder":"..."}),required=True)
    status = forms.ChoiceField(choices = StatusJob.CHOICES,required=True)

class AddJobSeek(forms.Form):
    job = forms.ModelChoiceField(queryset=Job.objects.all(),required=True)
    candidate = forms.ModelChoiceField(queryset=Candidate.objects.all(),required=True)
    offer = forms.IntegerField(widget=forms.NumberInput,required=True)
    offer_definition = forms.CharField(widget=forms.TextInput, required=False)
    release_date = forms.DateField(widget=NumberInput(attrs={'type': 'date', "class":"form-control", "placeholder":"01.01.1999"}))
    denial_status = forms.ChoiceField(choices = DenialStatus.CHOICES,required=True)
    call_status = forms.ChoiceField(choices = CallStatus.CHOICES,required=True)
    call_status_defenition = forms.CharField(widget=forms.TextInput, required=False)
    test_status = forms.ChoiceField(choices = TestStatus.CHOICES,required=True)
    test_status_defenition = forms.CharField(widget=forms.TextInput, required=False)
    meet_status = forms.ChoiceField(choices = MeetStatus.CHOICES,required=True)
    meet_status_defenition = forms.CharField(widget=forms.TextInput, required=False)
    meetemp_status = forms.ChoiceField(choices = MeetEmpStatus.CHOICES,required=True)
    meetemp_status_defenition = forms.CharField(widget=forms.TextInput, required=False)

class UploadHTMLFile(forms.Form):
    file = forms.FileField(widget=forms.FileInput(attrs={'class': ''}))