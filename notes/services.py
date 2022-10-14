from notes.models import NoteCategory


def create_default_categories():
    default_categories = ['Ссылка', 'Заметка', 'Памятка', 'TODO']
    categories_to_create = []
    for category_name in default_categories:
        categories_to_create.append(
            NoteCategory(
                title=category_name
            )
        )
    NoteCategory.objects.bulk_create(categories_to_create)