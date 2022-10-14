import datetime

from django.contrib.auth.mixins import AccessMixin
from django.urls import reverse_lazy
from django.views.generic import ListView, CreateView, UpdateView, DetailView, DeleteView

from notes.forms import NoteForm
from notes.models import Note, NoteCategory


class NotesListView(AccessMixin, ListView):
    model = Note
    paginate_by = 1

    def is_ajax(self):
        return self.request.headers.get('x-requested-with') == 'XMLHttpRequest'

    def get(self, *args, **kwargs):
        self.object_list = self.get_queryset()
        if self.is_ajax() and self.paginate_by:
            self.template_name = 'notes/includes/notes_ajax_list.html'
        return super().get(*args, **kwargs)

    def get_context_data(self, *args, **kwargs):
        context_data = super().get_context_data(*args, **kwargs)
        context_data['categories'] = NoteCategory.objects.all()
        return context_data

    def get_queryset(self):
        queryset = super().get_queryset().filter(owner=self.request.user, is_active=True)
        # if self.is_ajax():
        if self.request.GET.get('dfrom', None):
            d_from = self.request.GET.get('dfrom')
            d_from = datetime.datetime.strptime(d_from, "%Y-%m-%d")
            queryset = queryset.filter(created_at__gte=d_from)

        if self.request.GET.get('dto', None):
            d_to = self.request.GET.get('dto')
            d_to = datetime.datetime.strptime(d_to, "%Y-%m-%d")
            queryset = queryset.filter(created_at__lte=d_to)

        if self.request.GET.get('search'):
            queryset = queryset.filter(title__icontains=self.request.GET.get('search'))

        if self.request.GET.get('favorites'):
            favorites = int(self.request.GET.get('favorites'))
            if favorites >= 0:
                queryset = queryset.filter(favorites=bool(favorites))

        if self.request.GET.get('published'):
            published = int(self.request.GET.get('published'))
            if published >= 0:
                queryset = queryset.filter(published=bool(published))

        if self.request.GET.get('category'):
            cat_id = int(self.request.GET.get('category'))
            if cat_id > 0:
                queryset = queryset.filter(category_id=cat_id)

        return queryset


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

