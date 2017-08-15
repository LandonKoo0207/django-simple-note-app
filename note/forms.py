from django import forms
from .models import Note
from datetime import datetime

class NoteForm(forms.ModelForm):
	title = forms.CharField(max_length=50, required=True)
	content = form.TextField(required=True)
    time_updated = forms.DateTimeField(widget=forms.HiddenInput())

	class Meta:
		model = Note
		fields = ('title', 'content', 'time_updated')
