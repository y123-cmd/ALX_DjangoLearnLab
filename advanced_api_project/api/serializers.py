from rest_framework import serializers
from .models import Author, Book

class BookSerializer(serializers.ModelSerializer):
  """
    Serializer for the Book model.
    Validates that the publication year is not in the future.
    """
    class Meta:
        model = Book
        fields = '__all__'

    # Custom validation for publication_year
    def validate_publication_year(self, value):
        if value > 2024:  # Set current year as max
            raise serializers.ValidationError("Publication year cannot be in the future.")
        return value

class AuthorSerializer(serializers.ModelSerializer):
    books = BookSerializer(many=True, read_only=True)  # Nested BookSerializer

    class Meta:
        model = Author
        fields = ['name', 'books']
