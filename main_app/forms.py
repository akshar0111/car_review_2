from .models import car, review
from django.forms import ModelForm

class car_form(ModelForm):
    class Meta:
        model = car
        fields = '__all__'

class review_form(ModelForm):
    class Meta:
        model = review
        fields = '__all__'
