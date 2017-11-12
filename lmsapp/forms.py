from django import forms
from.models import LmsPost

class LmsPostForm(forms.ModelForm):
	class Meta:
		model =LmsPost
		fields =('name','faculty','book','borrowed','duedate')

	def __init__(self, *args, **kwargs):
		super(LmsPostForm, self).__init__(*args, **kwargs)
		self.fields['borrowed'].widget.attrs={
			'placeholder': 'MM/DD/YYYY'}