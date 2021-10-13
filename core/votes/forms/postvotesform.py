from django.forms import ModelForm
from django import forms
from votes.models import votesModel

class VotesForm(ModelForm):

    class Meta: 
        model = votesModel 
        fields = [ 'id','title', 'body', 'categorys','isclosed']
