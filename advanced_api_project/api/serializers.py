from rest_framework import serializers
from .models import Author, Book

class BookSerializer(serializers.ModelSerializer):
 """
    Serializer for the Book model. Includes custom validation to prevent future publication years.
    """
    ...
    class Meta:
        model = Book
        fields = ['title', 'publication_year', 'author']

    def validate_publication_year(self, value):
        """
        Ensure the publication year is not in the future.
        """
        if value > 2024:  # Customize the year based on your need
            raise serializers.ValidationError("Publication year cannot be in the future.")
        return value

class AuthorSerializer(serializers.ModelSerializer):
"""
    Serializer for the Author model. Includes a nested BookSerializer to serialize related books.
    """
    ...
    books = BookSerializer(many=True, read_only=True)  # Nested serializer for related books

    class Meta:
        model = Author
        fields = ['name', 'books']

