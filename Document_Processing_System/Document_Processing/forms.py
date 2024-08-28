from django import forms 
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm 
from .models import Document
from django import forms 
  
  
class UserRegisterForm(UserCreationForm): 
    email = forms.EmailField() 
    phone_no = forms.CharField(max_length = 20) 
    first_name = forms.CharField(max_length = 20) 
    last_name = forms.CharField(max_length = 20) 
    class Meta: 
        model = User 
        fields = ['username', 'email', 'phone_no', 'password1', 'password2']

class DocumentForm(forms.ModelForm):  
    class Meta:  
        model = Document
        fields = "__all__"
 
    def __init__(self, *args, **kwargs):
            super(DocumentForm, self).__init__(*args, **kwargs)
            for field_name, field in self.fields.items():
                field.widget.attrs['class'] = 'form-control' 