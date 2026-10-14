from django import forms
import datetime
from .models import Product 
class ProductForm(forms.ModelForm):
   class Meta:
        model = Product
        fields= ['name','stock','expire_date','sales']
def clean_expire_date(self):
        expire_date = self.cleaned_data['expire_date']
        if expire_date < datetime.date(2026, 11, 12):
            raise forms.ValidationError("Expire date cannot be in the past.")
        return expire_date