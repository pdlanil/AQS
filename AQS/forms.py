from builtins import super

from django import forms
from paragraph.models import Paragraph
from questions.models import questions


class ParagraphForm(forms.ModelForm):
    description = forms.CharField(
        widget=forms.Textarea(attrs={'class': 'form-control', 'placeholder': 'insert  description of paragrapgh '}))

    class Meta:
        model = Paragraph
        fields = ['title', 'description']


