from django.shortcuts import render
from .models import Notes #importing models that is created

from django.views.generic import CreateView, ListView ,DetailView, UpdateView,DeleteView
from .forms import NotesForm   #importing notesform

# Create your views here.
class NotesDeleteView(DeleteView):
    model = Notes
    success_url = '/smart/notes/'
    template_name ='notes/notes_delete.html'    # for solving naming error
    

class NotesUpdateView(UpdateView):
    model = Notes
    success_url = '/smart/notes/'
    form_class = NotesForm

class NotesCreateView(CreateView):
    model = Notes
 
    #after successful creation of  new note, allows user to go  -- all list of notes
    success_url = '/smart/notes/'
    form_class = NotesForm      # fields = ['title', 'text']  # notes contain title and content text only

class NotesListView(ListView):
    model = Notes 
    context_object_name = "notes"

#replace by NotesListView class
''' 
    #lists all notes
# def list(request):
#     all_notes = Notes.objects.all() #gets all notes 
#     return render(request, 'notes/notes_list.html', {'notes': all_notes}) # renders created destination to notes template # defines notes
'''

class NotesDetailView(DetailView):
    model = Notes
    context_object_name = "notes"

# replaced by NotesDetailView
'''
     #Displaying Contents Of A Single Note
# def detail(request, pk): #pk -- primary key of db

#     #note is for single
#     note = Notes.objects.get(pk=pk)  #pk is set as default
#     return render(request, 'notes/notes_detail.html', {'note': note}) #specifying name as note to variable note
'''