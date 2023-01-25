from .models import Comment
from django import forms

from django_summernote.widgets import SummernoteInplaceWidget, SummernoteWidget

class CommentForm(forms.ModelForm):
    class Meta:
        model = Comment
        fields = ('name', 'email', 'body')

class SomeForm(forms.Form):
    foo = forms.CharField(widget = SummernoteWidget()) #instead of forms.Textarea

# While rendering the content in templates use the safe filter which prevents HTML from escaping.
# {{ content | safe }}
