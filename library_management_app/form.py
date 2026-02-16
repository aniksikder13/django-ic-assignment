from django import forms
from .models import Book

class BookForm(forms.ModelForm):
    class Meta:
        model= Book
        fields= '__all__'
        
        widgets = {
            "title": forms.TextInput(attrs={"class": "input-field"}),
            "description": forms.Textarea(attrs={"class": "input-field", "rows": 4}),
            "published_date": forms.DateInput(attrs={
                "type": "date",
                "class": "input-field"
            }),
            "category": forms.Select(attrs={"class": "input-field"}),
            "author": forms.SelectMultiple(attrs={"class": "input-field"}),
            "status": forms.CheckboxInput(attrs={"class": "checkbox-field"}),
        }