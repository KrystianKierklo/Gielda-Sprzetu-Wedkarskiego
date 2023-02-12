from django import forms

from .models import Item

class NewItemForm(forms.ModelForm):
    class Meta:
        model = Item
        fields = ('category', 'name', 'description', 'price', 'image')

        widgets = {
            'category': forms.Select(attrs={
                'class': 'w-full py-5 px-6 rounded-xl border',
            }),

            'name': forms.TextInput(attrs={
                'placeholder': 'Wprowadź nazwę dodawanego przedmiotu',
                'class': 'w-full py-5 px-6 rounded-xl border'
            }),

            'description': forms.Textarea(attrs={
                'placeholder': 'Napisz kilka słów o dodawanym produkcie',
                'class': 'w-full py-5 px-6 rounded-xl border'
            }),

            'price': forms.TextInput(attrs={
                'placeholder': 'Wprowadź cenę produktu',
                'class': 'w-full py-5 px-6 rounded-xl border'
            }),

            'image': forms.FileInput(attrs={
                'class': 'w-full py-5 px-6 rounded-xl border'
            })
        }

class EditItemForm(forms.ModelForm):
    class Meta:
        model = Item
        fields = ('name', 'description', 'price', 'image')

        widgets = {
            'name': forms.TextInput(attrs={
                'placeholder': 'Wprowadź nazwę dodawanego przedmiotu',
                'class': 'w-full py-5 px-6 rounded-xl border'
            }),

            'description': forms.Textarea(attrs={
                'placeholder': 'Napisz kilka słów o dodawanym produkcie',
                'class': 'w-full py-5 px-6 rounded-xl border'
            }),

            'price': forms.TextInput(attrs={
                'placeholder': 'Wprowadź cenę produktu',
                'class': 'w-full py-5 px-6 rounded-xl border'
            }),

            'image': forms.FileInput(attrs={
                'class': 'w-full py-5 px-6 rounded-xl border'
            })
        }

