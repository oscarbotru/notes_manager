from django.urls import path
from notes.views import NotesListView, NotesCreateView, NotesUpdateView, NotesDetailView, NotesDeleteView
from notes.apps import NotesConfig

app_name = NotesConfig.name


urlpatterns = [
    path('', NotesListView.as_view(), name='list'),
    path('create/', NotesCreateView.as_view(), name='create'),
    path('edit/<pk>/', NotesUpdateView.as_view(), name='update'),
    path('view/<pk>/', NotesDetailView.as_view(), name='detail'),
    path('delete/<pk>/', NotesDeleteView.as_view(), name='delete'),
]
