from django.forms import ModelForm
from django import forms 
from .models import Comment


class CommentForm(forms.ModelForm):
	class Meta:
		model = Comment
		fields = ('name','email', 'comment_text')

		def __init__(self, *args, **kwargs):
			super(CommentForm, self).__init__(*args, **kwargs)