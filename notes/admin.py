from django.contrib import admin
from . import models

# Register your models here.
class NotesAdmin(admin.ModelAdmin):

    list_display = ('title',)  #for notes title detail (not anonymous)

admin.site.register(models.Notes, NotesAdmin) #registering models.Notes and NotesAdmin