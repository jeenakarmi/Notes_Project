from django import forms  #to put forms
from .models import Notes   #with models imported Notes

class NotesForm(forms.ModelForm):
    class Meta:
        model = Notes
        fields = ('title' , 'text')

        # for layout 
        # my-3:margin
        widgets = {
            'title' : forms.TextInput(attrs={'class' : 'form-control my-3'}),
            'text' : forms.Textarea(attrs={'class' : 'form-control my-3'}),
        }

        # for naming noteContent-Title
        labels ={
            'title': 'Title',
            'text' : 'Your Note' 
        }

'''
    #only for django notes 
    def clean_title(self):
        title = self.cleaned_data['title']
        if 'Django' not in title:
            raise forms.ValidationError('Notes Should be about Django only! ')
        return title
'''
