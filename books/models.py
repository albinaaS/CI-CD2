from django.db import models
from django.utils import timezone

class Author(models.Model):
    db_table = "Autors"
    name = models.CharField(max_length=100)
    bio = models.TextField()

    def __str__(self):
        return self.name


class Book(models.Model):
    db_table = "Books"
    title = models.CharField(max_length=100)
    authors = models.ManyToManyField(Author)
    description = models.TextField()
    publication_date = models.DateField()
    cover_image = models.ImageField(upload_to='book_covers/')
    price = models.DecimalField(max_digits=6, decimal_places=2)

    def __str__(self):
        return self.title

    @classmethod
    def Books(cls):
        today = timezone.now().date()
        return cls.objects.filter(publication_date__gte=today)

    @classmethod
    def get_books(cls, primary_key):
        return cls.objects.get(pk=primary_key)