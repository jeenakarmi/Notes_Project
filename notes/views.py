from django.shortcuts import render
from .models import Notes #importing models that is created

# Create your views here.
    #lists all notes
def list(request):
    all_notes = Notes.objects.all() #gets all notes 
    return render(request, 'notes/notes_list.html', {'notes': all_notes}) # renders created destination to notes template # defines notes