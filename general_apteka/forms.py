from django import forms
from .models import  Product, Reviev, Question

class RevievAddForm(forms.Form):
	heading_reviev = forms.CharField()
	text_reviev = forms.CharField()


class QuestionForm(forms.ModelForm):
    name = forms.CharField()
    email = forms.EmailField()
    text = forms.CharField(widget=forms.Textarea)

    class Meta:
        model = Question
        fields = ['name', 'email', 'text'] 

