from django import forms  #to put forms
from .models import Notes   #with models imported Notes

class NotesForm(forms.ModelForm):
    class Meta:
        model = Notes
        fields = ('title' , 'text')
        
'''
    #only for django notes 
    def clean_title(self):
        title = self.cleaned_data['title']
        if 'Django' not in title:
            raise forms.ValidationError('Notes Should be about Django only! ')
        return title

'''   