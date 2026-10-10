from django import forms


class FormEmployee (forms.Form):

    POSITION = (
        (1, 'Chef'),
        (2, 'Administrator'),
        (3, 'Waiter'),
        (4, 'Assistant'),
    )


    name = forms.CharField(
        required=True,
        max_length=25,
        widget=forms.TextInput(attrs={'class': 'inputs-form-employee mb-1'})
    )

    lastname = forms.CharField(
        required=True,
        max_length=20,
        widget=forms.TextInput(attrs={'class': 'inputs-form-employee mb-1'})
    )

    photo = forms.CharField(
        required=True,
        max_length=20,
        widget=forms.TextInput(attrs={'class': 'inputs-form-employee mb-1'})
    )

    salary = forms.CharField(
        required=True,
        max_length=12,
        widget=forms.NumberInput(attrs={'class': 'inputs-form-employee mb-1'})
    )

    contact = forms.CharField(
        required=True,
        max_length=20,
        widget=forms.NumberInput(attrs={'class': 'inputs-form-employee mb-1'})
    )

    cargo = forms.ChoiceField(
        required=True,
        label='',
        widget=forms.Select(attrs={'class': 'inputs-form-employee mb-1'}),
        choices=POSITION
    )
