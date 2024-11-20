from rest_framework import generics
from .models import Book  # Assuming you have a Book model
from .serializers import BookSerializer  # Assuming you have a BookSerializer

class BookList(generics.ListAPIView):
    queryset = Book.objects.all()  # Get all books from the database
    serializer_class = BookSerializer  # Use the BookSerializer to format the data

