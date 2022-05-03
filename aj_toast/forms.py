from .models import ToastSettings
from django import forms


class ToastForm(forms.ModelForm):
	def __init__(self, *args, **kwargs):
		super(ToastForm, self).__init__(*args, **kwargs)


		for visible in self.visible_fields():
			visible.field.widget.attrs['class'] = 'form-control form-control-sm'
		
		self.fields['Close_Button'].widget.attrs['class'] = 'Close_Button	'
		self.fields['Newest_on_top'].widget.attrs['class'] = 'Newest_on_top	'
		self.fields['Add_behavior_click'].widget.attrs['class'] = 'Add_behavior_click	'
		self.fields['Progress_Bar'].widget.attrs['class'] = 'Progress_Bar	'
		self.fields['Prevent_Duplicates'].widget.attrs['class'] = 'Prevent_Duplicates	'
			
			

	class Meta:
		model = ToastSettings
		fields = '__all__'
