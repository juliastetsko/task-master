from django import forms


class TaskSearchForm(forms.Form):
    name = forms.CharField(
        max_length=255,
        required=False,
        label="",
        widget=forms.TextInput(
            attrs={
                "placeholder": "Search by name"
            }
        )
    )
    assignee = forms.CharField(
        max_length=255,
        required=False,
        label="",
        widget=forms.TextInput(
            attrs={
                "placeholder": "Search by assignee"
            }
        )
    )
    include_completed = forms.BooleanField(
        required=False,
        widget=forms.CheckboxInput(attrs={'onclick': 'this.form.submit();'}),
        label="Include completed"
    )
