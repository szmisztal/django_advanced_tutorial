from django.db import models
from .managers import BookManager
from django.core.validators import MaxValueValidator
from .validators import validate_year

class Genre():
    UNKNOWN = 0
    FANTASY = 1
    HORROR = 2
    DRAMA = 3
    GENRES = (
        (UNKNOWN, 'Unknown'),
        (FANTASY, 'Fantasy'),
        (HORROR, 'Horror'),
        (DRAMA, 'Drama')
    )

class Author(models.Model):
    name = models.CharField(max_length = 20, blank = False)
    surname = models.CharField(max_length = 20, blank = False)
    birthday = models.DateField(null = True, blank = True, default = None)

    def __str__(self):
        return f"{self.name} {self.surname}"

class Book(models.Model):
    title = models.CharField(max_length = 50, blank = False)
    publication_year = models.IntegerField(blank = False, validators = [
        MaxValueValidator(2023)])
    author = models.ForeignKey(Author, on_delete = models.CASCADE, related_name = 'books')
    genre = models.PositiveSmallIntegerField(choices = Genre.GENRES, default = 0)

    objects = models.Manager()
    books = BookManager()

    def save(self, *args, **kwargs):
        validate_year(self.publication_year)
        super(Book, self).save(*args, **kwargs)

    def is_new(self):
        return True if self.publication_year > 1980 else False

    def __str__(self):
        return f"{self.title}"

    class Meta:
        # db_table = "books"
        # ordering = ['publication_year']
        # order_with_respect_to = 'author'
        verbose_name = "Book"
        verbose_name_plural = "Books"
        unique_together = [
            ["title", "publication_year"]
        ]
        indexes = [
            models.Index(fields = ["title"], name = "title_inx"),
            models.Index(fields = ["title", "publication_year"])
        ]
        permissions = [
            ("can_update_book", "Can change book")
        ]
