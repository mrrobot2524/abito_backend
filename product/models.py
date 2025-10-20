from django.db import models
from PIL import Image
import os

class Item(models.Model):
    title = models.CharField(max_length=255)
    descriptions = models.TextField(null=True, blank=True)
    price = models.DecimalField(max_digits=10, decimal_places=2)
    address = models.CharField(max_length=255)
    date = models.DateTimeField()
    img = models.ImageField(upload_to='items/', blank=True, null=True)

    def save(self, *args, **kwargs):
        super().save(*args, **kwargs)

        if self.img:
            img_path = self.img.path
            img = Image.open(img_path)
            img = img.convert("RGB")

            max_width, max_height = 265, 179

            # Текущее разрешение
            width, height = img.size

            # Проверяем, нужно ли уменьшать
            if width > max_width or height > max_height:
                img.thumbnail((max_width, max_height), Image.Resampling.LANCZOS)
                img.save(img_path, quality=90)

    def __str__(self):
        return f"{self.title} — {self.price}"


# http://127.0.0.1:8000/api/product/