from django import forms
from .models import RegisterStudent


class RegisterForm(forms.ModelForm):
    class Meta:
        model = RegisterStudent
        fields = "__all__"

class RegiserFormCustom(forms.Form):
    teamName = forms.CharField(label="Название команды:",widget=forms.TextInput(attrs={"required class":"win_reg_input"}))
    email = forms.EmailField(label="Почта:",widget=forms.EmailInput(attrs={"required class":"win_reg_input"}))
    number = forms.IntegerField(label="Номер Телефона:",widget=forms.NumberInput(attrs={"required class":"win_reg_input"}))
    fioOne = forms.CharField(label="ФИО первого учстника:",widget=forms.TextInput(attrs={"class":"win_reg_input"}))
    fioSecond = forms.CharField(label="ФИО второго учстника:",widget=forms.TextInput(attrs={"class":"win_reg_input"}))
    fioThree = forms.CharField(required=False,label="ФИО третьего учстника:",widget=forms.TextInput(attrs={"class":"win_reg_input"}))
    fioFour = forms.CharField(required=False,label="ФИО четвертого учстника:",widget=forms.TextInput(attrs={"class":"win_reg_input"}))
    fioFive = forms.CharField(required=False,label="ФИО пятого учстника:",widget=forms.TextInput(attrs={"class":"win_reg_input"}))
    university_name = forms.CharField(required=False,label="Учебное завдение:",widget=forms.TextInput(attrs={"class":"win_reg_input"}))