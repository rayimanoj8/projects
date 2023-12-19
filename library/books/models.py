from datetime import timedelta
from django.utils import timezone
from django.db import models
from django.contrib.auth.models import User


# Create your models here.
class Book(models.Model):
    book_title = models.CharField(max_length=100)
    book_author = models.CharField(max_length=100)
    isbn = models.CharField(max_length=13, unique=True)
    is_available = models.BooleanField(default=True)
    book_image = models.ImageField(default="default.jpg")

    def __init(self, title, author, isbn, is_availabe):
        self.book_title = title
        self.book_author = author
        self.isbn = isbn
        self.is_available = is_availabe

    def __str__(self):
        return f"{self.book_title} by {self.book_author}"


class Books_taken(models.Model):
    user_id = models.ForeignKey(User, on_delete=models.CASCADE)
    book_id = models.ForeignKey(Book, on_delete=models.CASCADE)
    return_date = models.DateTimeField(default=timezone.now() + timedelta(days=5))

    def fine(self):
        days_diff = self.return_date-timezone.now()
        if days_diff.days>5:
           return days_diff.days-5*5
        return 0

    def __str__(self):
        return f"{self.book_id.book_title} taken by {self.user_id.username} on {self.return_date}"
