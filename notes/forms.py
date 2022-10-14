from django import forms

from notes.models import Note


class NoteForm(forms.ModelForm):

    class Meta:
        model = Note
        fields = ('title', 'body', 'category', 'favorites', 'published')

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        for field_name, field in self.fields.items():
            field.widget.attrs['class'] = 'form-control'
