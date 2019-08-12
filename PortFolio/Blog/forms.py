from django import forms

class CommentForm(forms.Form):
    author = forms.CharField(
        max_length=80,
        widget=forms.TextInput(attrs={
            "class": "form-control",
            "placeholder": "Your Name",
        })
    )
    detail = forms.CharField(widget=forms.Textarea(
        attrs={
            "class": 'forms-control',
            'placeholder': "Leave a comment!",
        })
    )
