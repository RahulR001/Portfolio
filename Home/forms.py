from django import forms
from .models import contact


# ========== class-to-generate-contact-from ==========

class contactform(forms.ModelForm):
    class Meta:
        model = contact
        fields = '__all__'



