from django import forms

class ProfileForm(forms.Form):
    profile_picture = forms.FileField(
        label='Profile Picture',
        required=False,
        help_text='Upload a profile picture (optional).'
    )

    