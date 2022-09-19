from django.db import models
from .utilities import get_timestamp_path
from PIL import Image


# Client model
class Client(models.Model):

    # Options for 'sex' field
    SEX_CHOICES = (
        ("m", "Мужской"),
        ("f", "Женский"),
        ('u', 'Не указан'),
    )

    name = models.CharField(max_length=50, verbose_name='Имя')
    last_name = models.CharField(max_length=50, verbose_name='Фамилия')
    birthday = models.DateField(verbose_name='Дата рождения')
    sex = models.CharField(max_length=1, choices=SEX_CHOICES, default='u', verbose_name='Пол')


# Client photo model
class ClientImage(models.Model):
    client = models.OneToOneField(Client, on_delete=models.CASCADE, related_name='clientimage', verbose_name='Клиент')
    image = models.ImageField(upload_to=get_timestamp_path, verbose_name='Изображение')

    def save(self, crop_values=None, *args, **kwargs):
        # Save default image
        super().save()

        # Open image using self
        img = Image.open(self.image.path)

        img = img.crop(crop_values)

        # Save image at the same path
        img.save(self.image.path)

