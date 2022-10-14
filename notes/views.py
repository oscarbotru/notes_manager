from django.contrib.auth.mixins import AccessMixin
from django.urls import reverse_lazy
from django.views.generic import ListView, CreateView, UpdateView, DetailView, DeleteView

from notes.forms import NoteForm
from notes.models import Note


class NotesListView(AccessMixin, ListView):
    model = Note

    def get_queryset(self):
        return super().get_queryset().filter(owner=self.request.user, is_active=True)


class NotesCreateView(AccessMixin, CreateView):
    model = Note
    form_class = NoteForm
    success_url = reverse_lazy('notes:list')

    def form_valid(self, form):
        self.object = form.save(commit=False)
        self.object.owner = self.request.user
        self.object.save()
        return super().form_valid(form)


class NotesUpdateView(AccessMixin, UpdateView):
    model = Note
    form_class = NoteForm
    success_url = reverse_lazy('notes:list')


class NotesDetailView(AccessMixin, DetailView):
    model = Note


class NotesDeleteView(AccessMixin, DeleteView):
    model = Note

