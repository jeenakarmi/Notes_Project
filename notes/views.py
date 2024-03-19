from django.shortcuts import render
from .models import Notes #importing models that is created

from django.views.generic import ListView

# Create your views here.

class NotesListView(ListView):
    model = Notes 
    context_object_name = "notes"

#replace by NotesListView class
#     #lists all notes
# def list(request):
#     all_notes = Notes.objects.all() #gets all notes 
#     return render(request, 'notes/notes_list.html', {'notes': all_notes}) # renders created destination to notes template # defines notes


#Displaying Contents Of A Single Note
def detail(request, pk): #pk -- primary key of db

    #note is for single
    note = Notes.objects.get(pk=pk)  #pk is set as default
    return render(request, 'notes/notes_detail.html', {'note': note}) #specifying name as note to variable note