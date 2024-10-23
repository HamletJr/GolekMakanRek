from django.db import models
import uuid
from django.contrib.auth.models import User
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

    @property
    def average_rating(self):
        avg_rating = self.foodrating_set.aggregate(Avg('rating'))['rating__avg']
        return round(avg_rating, 2) if avg_rating is not None else 0
    
    @property
    def total_reviews(self):
        return self.foodrating_set.count()

    def __str__(self):
        return self.nama

class FoodRating(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    deskripsi_food = models.ForeignKey(Food, on_delete=models.CASCADE)
    rating = models.IntegerField()
    comment = models.TextField(blank=True, null=True)
    waktu_comment = models.DateTimeField(auto_now_add=True)

    class Meta:
        constraints = [
            models.CheckConstraint(check=models.Q(rating__gte=1, rating__lte=5), name="rating")
        ] 