from django.forms import ModelForm
from.models import *
from.templates.daycare_app import *
 #create forms related to models
 
class Signupform(ModelForm):
    class Meta:
         model = Signup
         fields = "__all__"

class Loginform(ModelForm):
    class Meta:
         model = Login
         fields = "__all__"