from django.db import models
import uuid
from django.db.models import Avg

class Restaurant(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    nama = models.CharField(max_length=255)
    kategori = models.CharField(max_length=255)
    deskripsi = models.TextField()

    def __str__(self):
        return self.nama

class Food(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    nama = models.CharField(max_length=255)
    kategori = models.CharField(max_length=255)
    harga = models.IntegerField()
    diskon = models.IntegerField()
    deskripsi = models.TextField()
    restoran = models.ForeignKey(Restaurant, on_delete=models.CASCADE)
    image_url = models.URLField(max_length=200, blank=True, null=True)

    @property
    def average_rating(self):
        avg_rating = self.foodrating_set.aggregate(Avg('rating'))['rating__avg']
        return round(avg_rating, 2) if avg_rating is not None else 0
    
    @property
    def total_reviews(self):
        return self.foodrating_set.count()

    def __str__(self):
        return self.nama