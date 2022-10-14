import uuid

from django.db import models

from users.models import User


class NoteCategory(models.Model):
    title = models.CharField(max_length=150, verbose_name='Заголовок')

    class Meta:
        verbose_name = 'категория заметок'
        verbose_name_plural = 'категории заметок'

    def __str__(self):
        return f'{self.title}'


class Note(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)

    title = models.CharField(max_length=150, verbose_name='Заголовок')
    body = models.TextField(verbose_name='Содержимое')

    category = models.ForeignKey(NoteCategory, on_delete=models.CASCADE, verbose_name='Категория')
    favorites = models.BooleanField(default=False, verbose_name='Избранное')
    published = models.BooleanField(default=False, verbose_name='Опубликовано')
    owner = models.ForeignKey(User, on_delete=models.CASCADE, verbose_name='Владелец заметки')

    # Хорошим тоном является не удаление сущности, а отметка о неиспользовании
    is_active = models.BooleanField(default=True, verbose_name='Активна')
    created_at = models.DateTimeField(auto_now_add=True, verbose_name='Дата создания')
    # Для удобной работы с возражениями пользователей лучше сохранять весь журнал активности, но минимум дату обновления
    updated_at = models.DateTimeField(auto_now=True, verbose_name='Дата обновления')

    class Meta:
        verbose_name = 'заметка'
        verbose_name_plural = 'заметки'

    def __str__(self):
        return f'{self.title}'
