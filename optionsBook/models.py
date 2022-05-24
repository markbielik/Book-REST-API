from django.db import models
from django.urls import reverse


class Books(models.Model):
    external_id = models.CharField(verbose_name='external_id',
                                   max_length=100,
                                   blank=True)
    title = models.CharField(verbose_name='title',
                             max_length=255)
    authors = models.CharField(verbose_name='authors',
                               max_length=300)
    publication_year = models.PositiveIntegerField(verbose_name='published_year')
    acquired_state = models.BooleanField(verbose_name='acquired',
                                         default=True)
    thumbnail = models.CharField(verbose_name='thumbnail',
                                 max_length=300,
                                 blank=True)

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse('book_detail', args=(self.pk,))

