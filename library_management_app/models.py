import uuid
from django.db import models

class Category(models.Model):
    id = models.UUIDField(primary_key=True, editable=False, default=uuid.uuid4)
    name = models.CharField(max_length=255)
    summery = models.TextField(max_length=500)
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        db_table = "category"

    def __str__(self):
        return f"{self.name} - {self.created_at}"


class Author(models.Model):
    id = models.UUIDField(primary_key=True, editable=False, default=uuid.uuid4)
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    date_of_birth = models.DateField(null=True, blank=True)
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        db_table = "author"

    def __str__(self):
        return f"{self.first_name} {self.last_name} - {self.created_at}"


class Book(models.Model):
    id = models.UUIDField(primary_key=True, editable=False, default=uuid.uuid4)
    title = models.CharField(max_length=255)
    description = models.TextField(max_length=1000)
    status = models.BooleanField(default=True)
    published_date = models.DateField(null=True, blank=True)
    created_at = models.DateTimeField(auto_now_add=True)

    author = models.ManyToManyField(Author, related_name="books")
    category = models.ForeignKey(Category, on_delete=models.CASCADE, related_name="books")

    class Meta:
        db_table = "book"

    def __str__(self):
        return f"{self.title} - {self.created_at}"