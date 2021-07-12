from django import forms


class TestForm(forms.Form):
    main_message = forms.CharField(max_length=100)
