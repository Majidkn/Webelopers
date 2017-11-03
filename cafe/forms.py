from django.forms.models import ModelForm
from .models import Comment
from .models import Cafe


class CommentForm(ModelForm):
    class Meta:
        model = Comment
        fields = ('text',)