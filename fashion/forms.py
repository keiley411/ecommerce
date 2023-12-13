from django.contrib.auth.models import User
from django import forms
from .import models

class CustomerUserForm(forms.ModelForm):
    class Meta:
        model = User
        fields = ['first_name', 'last_name', 'username', 'password']
        widgets = {
            'password': forms.PasswordInput()
        }

class CustomerForm(forms.ModelForm):
    class Meta:
        model = models.Customer
        fields = ['address','mobile','profile_pic']

class ProductForm(forms.ModelForm):
    class Meta:
        model=models.Product
        fields=['name','price','description','product_image']


#address of shipment
class AddressForm(forms.Form):
    Email = forms.EmailField()
    Mobile= forms.IntegerField()
    Address = forms.CharField(max_length=500)

class FeedbackForm(forms.Form):
    class Meta:
        model=models.Feedback
        fields=['name','feedback', 'message']

    def save(self, commit =True):
        instance = super(FeedbackForm, self).save(commit=False)
        if commit:
            instance.save()
            return instance


#for updating status of order
class OrderForm(forms.ModelForm):
    class Meta:
        model=models.Orders
        fields=['status']

#for contact us page
class ContactusForm(forms.Form):
    Name = forms.CharField(max_length=30)
    Email = forms.EmailField()
    Message = forms.CharField(max_length=500,widget=forms.Textarea(attrs={'rows': 3, 'cols': 30}))
