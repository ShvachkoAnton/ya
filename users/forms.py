from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import get_user_model
from django import forms


#шаблон для регистрации
User=get_user_model()
class CreationForm(UserCreationForm):
    class Meta(UserCreationForm.Meta):
        model=User
        fields=("first_name","last_name","username","email")
#виджеты, продолжение в shellplus
class Name(forms.Form):
    subject=forms.CharField(label='your name',max_length=25)
    message=forms.CharField(widget=forms.Textarea)
    sender=forms.EmailField()
    cc_myself=forms.BooleanField(label='так',required=False)


class validator(forms.Form):
    subject=forms.CharField(max_length=100)
    message=forms.CharField(widget=forms.Textarea)
    sender=forms.EmailField()
    cc_myself=forms.BooleanField(required=False)
    def clean(self):
        data=self.cleaned_data['subject']
        if "спасибо" not in data.lower():
            raise forms.ValidationError('Валидатор формы subject')
        return data

    