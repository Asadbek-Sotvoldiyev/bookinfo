from django import forms
from .models import Comment

class CommentForm(forms.ModelForm):
    comment = forms.CharField(widget=forms.Textarea(attrs={'class':'commenttext','rows':5}))
    given_stars = forms.IntegerField(min_value=1,max_value=5,widget=forms.NumberInput(attrs={'class':'given'}))
    class Meta:
        model = Comment
        fields = ['comment', 'given_stars']