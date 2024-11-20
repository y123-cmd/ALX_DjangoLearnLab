from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from .models import Book
from .serializers import BookSerializer

class BookList(APIView):
    def get(self, request, format=None):
        books = Book.objects.all()  # Get all books from the database
        serializer = BookSerializer(books, many=True)  # Serialize the list of books
        return Response(serializer.data)  # Return the serialized data in the response

