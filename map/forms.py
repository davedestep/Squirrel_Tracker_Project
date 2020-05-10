from django.forms import ModelForm

from .models import Sighting

class SightingUpdateForm(ModelForm):
	class Meta:
		model = Sighting
		fields = '__all__'