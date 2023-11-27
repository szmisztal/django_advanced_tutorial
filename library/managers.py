from django.db import models

# class NewBookManager(models.Manager):
#     def get_queryset(self):
#         return super().get_queryset().filter(publication_year__gte = 1980)
#
# class OldBookManager(models.Manager):
#     def get_queryset(self):
#         return super().get_queryset().filter(publication_year__lt = 1980)

class BookQuerySet(models.QuerySet):
    def new_books(self):
        return self.filter(publication_year__gte = 1980)

    def old_books(self):
        return self.filter(publication_year__lt = 1980)

class BookManager(models.Manager):
    def get_queryset(self):
        return BookQuerySet(self.model, using = self._db)

    def new_books(self):
        return self.get_queryset().new_books()

    def old_books(self):
        return self.get_queryset().old_books()
