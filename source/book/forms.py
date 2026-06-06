from django import forms
from book.models import BookGuest


class BookGuestForm(forms.ModelForm):
    class Meta:
        model = BookGuest
        fields = ['author', 'email','content']
        widgets = {
            'author': forms.TextInput(attrs={'class':'form-control'}),
            'email': forms.EmailInput(attrs={'class':'form-control'}),
            'content': forms.Textarea(attrs={'class':'form-control'}),
        }