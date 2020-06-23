from django import forms

from backend.booking.models import Review


class PostForm(forms.ModelForm):
    image = forms.FileField(required=False)

    class Meta:
        model = Review
        fields = ['text', 'author_name', 'image']
