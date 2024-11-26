from django.db import models

class Author(models.Model):
    # Author name field
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name

class Book(models.Model):
    # Book title field
    title = models.CharField(max_length=255)
    # Publication year field
    publication_year = models.IntegerField()
    # Foreign Key relationship to Author
    author = models.ForeignKey(Author, related_name='books', on_delete=models.CASCADE)

    def __str__(self):
        return self.title

