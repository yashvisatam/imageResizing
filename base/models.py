from django.db import models
from PIL import Image, ImageOps

# Create your models here.
class Category(models.Model):
    title = models.CharField(max_length=200)

    class Meta:
        verbose_name = 'category'
        verbose_name_plural = 'categories'

    def __str__(self):
        return self.title

class News(models.Model):
    title = models.CharField(max_length=200)
    category = models.ForeignKey(Category, on_delete=models.CASCADE)  
    description = models.TextField()
    cover = models.ImageField(upload_to='covers/', blank=True)

    def save(self, *args, **kwargs):
        super().save(*args, **kwargs)
        img = Image.open(self.cover.path)
        img.show()

        thumbnail_img = img.resize((200,300))
        thumbnail_img.show()
        thumbnail_img.save(self.cover.path)

        medium_img = img.resize((500,500))
        medium_img.show()
        medium_img.save(self.cover.path)

        large_img = img.resize((1024,768))
        large_img.show()
        large_img.save(self.cover.path)

        grayscale_img = ImageOps.grayscale(img)
        grayscale_img.show()
        grayscale_img.save(self.cover.path)

    class Meta:
        verbose_name = 'news'
        verbose_name_plural = 'news'  

    def __str__(self):
        return self.title    
