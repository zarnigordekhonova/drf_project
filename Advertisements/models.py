from django.db import models


class Category(models.Model):
    name = models.CharField(max_length=124)

    class Meta:
        db_table = 'category'

    def __str__(self):
        return self.name


class Products(models.Model):
    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    name = models.CharField(max_length=250, blank=True, null=True)
    description = models.TextField()
    image = models.ImageField(upload_to='signs_images/', blank=True, null=True)
    video = models.FileField(upload_to='signs_videos/', blank=True, null=True)
    audio = models.FileField(upload_to='signs_audios/', blank=True, null=True)
    dock = models.FileField(upload_to='signs_dock/', blank=True, null=True)

    class Meta:
        db_table = 'roadsigns'

    def __str__(self):
        return f'{self.category.name} - {self.name}'
