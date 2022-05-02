from django.db import models


# Create your models here.


class Category(models.Model):
    name = models.CharField(max_length=40, null=False, blank=False)

    def __str__(self):
        return self.name
    
    class Meta:
        verbose_name_plural = 'Categories'


class Photo(models.Model):
    category = models.ForeignKey(Category, on_delete=models.SET_NULL, related_name='photo_categories', null=True)
    image = models.ImageField(upload_to='images', null=False, blank=False)
    description = models.TextField()

    def __str__(self):
        return str(self.image.url)

    class Meta:
        ordering = ['-category__name']
