from django.contrib import admin

from notes.models import NoteCategory, Note

admin.site.register(NoteCategory)
admin.site.register(Note)
