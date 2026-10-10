from django import forms

class FormPlates(forms.Form):
    PLATES = (
        (1, 'Caffe'),
        (2, 'Drinks'),
        (3, 'Alcohol'),
        (4, "Food"),
    )

    name = forms.CharField(
        required=True,
        max_length=20,
        label='Name',
        widget=forms.TextInput(attrs={'class': 'form-inputs mb-2'})
    )

    description = forms.CharField(
        required=True,
        max_length=200,
        label='Description',
        widget=forms.Textarea(attrs={'class': 'form-inputs text-area mb-2'})
    )

    image = forms.CharField(
        required=True,
        label='Image',
        widget=forms.TextInput(attrs={'class': 'form-inputs mb-2'})
    )

    price = forms.CharField(
        required=True,
        max_length=20,
        label='Price',
        widget=forms.NumberInput(attrs={'class': 'form-inputs mb-2'})
    )

    type = forms.ChoiceField(
        required=True,
        label='Type of dish',
        widget=forms.Select(attrs={'class': 'form-inputs mb-2'}),
        choices=PLATES
    )
