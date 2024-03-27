from typing import Any
from django.db.models.query import QuerySet
from django.shortcuts import render
from .models import Notes #importing models that is created

from django.views.generic import CreateView, ListView ,DetailView, UpdateView,DeleteView
from .forms import NotesForm   #importing notesform

from django.contrib.auth.mixins import LoginRequiredMixin

# Create your views here.
class NotesDeleteView(LoginRequiredMixin,DeleteView):
    model = Notes
    success_url = '/smart/notes/'
    template_name ='notes/notes_delete.html'    # for solving naming error
    login_url = "/admin/"  

    # available only for logged in users
    def get_queryset(self):
        return self.request.user.notes.all()
    

class NotesUpdateView(LoginRequiredMixin,UpdateView):
    model = Notes
    success_url = '/smart/notes/'
    form_class = NotesForm
    login_url = "/admin/"  

    # available only for logged in users
    def get_queryset(self):
        return self.request.user.notes.all()

class NotesCreateView(LoginRequiredMixin,CreateView):
    model = Notes
 
    #after successful creation of  new note, allows user to go  -- all list of notes
    success_url = '/smart/notes/'
    form_class = NotesForm      # fields = ['title', 'text']  # notes contain title and content text only
    login_url = "/admin/"  

    # available only for logged in users
    def get_queryset(self):
        return self.request.user.notes.all()

class NotesListView(LoginRequiredMixin, ListView):
    model = Notes 
    context_object_name = "notes"
    login_url = "/admin/"  

    # available only for logged in users
    def get_queryset(self):
        return self.request.user.notes.all()

#replace by NotesListView class
''' 
    #lists all notes
# def list(request):
#     all_notes = Notes.objects.all() #gets all notes 
#     return render(request, 'notes/notes_list.html', {'notes': all_notes}) # renders created destination to notes template # defines notes
'''

class NotesDetailView(LoginRequiredMixin,DetailView):
    model = Notes
    context_object_name = "notes"
    login_url = "/admin/"  

    # available only for logged in users
    def get_queryset(self):
        return self.request.user.notes.all()

# replaced by NotesDetailView
'''
     #Displaying Contents Of A Single Note
# def detail(request, pk): #pk -- primary key of db

#     #note is for single
#     note = Notes.objects.get(pk=pk)  #pk is set as default
#     return render(request, 'notes/notes_detail.html', {'note': note}) #specifying name as note to variable note
'''