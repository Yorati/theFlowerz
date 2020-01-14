from django.db import models
from django.urls import reverse #Used to generate URLs by reversing the URL patterns
import uuid # Required for unique instances
from django.db import IntegrityError
from django.contrib.auth.models import User
from datetime import date

class Color(models.Model):

    name = models.CharField(max_length=200, help_text="Введите цвет (Например: Желтый)")

    def __str__(self):
        """
        String for representing the Model object (in Admin site etc.)
        """
        return self.name

class Flower(models.Model):


    title = models.CharField(max_length=200)
    kind_of_flower = models.ForeignKey('KindOfFlower', on_delete=models.SET_NULL, null=True)

    summary = models.TextField(max_length=1000, help_text="Введите краткое описание")
    color = models.ManyToManyField(Color, help_text="Выбери цвета для букета")

    def __str__(self):
        """
        String for representing the Model object.
        """
        return self.title


    def get_absolute_url(self):
        """
        Returns the url to access a particular book instance.
        """
        return reverse('flower-detail', args=[str(self.id)])

    def display_color(self):
        return ', '.join([color.name for color in self.color.all()[:3]])
    display_color.short_description = 'Color'

class ForSale(models.Model):

    borrower = models.ForeignKey(User, on_delete=models.SET_NULL, null=True, blank=True)
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, help_text="Уникальный ID")
    flower = models.ForeignKey('Flower', on_delete=models.SET_NULL, null=True)
    imprint = models.CharField(max_length=200)

    LOAN_STATUS = (
        ('o', 'В наличии'),
        ('x', 'Нет в наличии'),
    )

    status = models.CharField(max_length=1, choices=LOAN_STATUS, blank=True, default='o', help_text='Есть/Нет в наличии')

    def __str__(self):
        """
        String for representing the Model object
        """
        return '%s (%s)' % (self.id,self.flower.title)
        class Meta:
            permissions = (("can_mark_returned", "Set flower as returned"),)

class KindOfFlower(models.Model):

    name = models.CharField(max_length=100)
    def get_absolute_url(self):
        """
        Returns the url to access a particular author instance.
        """
        return reverse('kind_of_flower-detail', args=[str(self.id)])


    def __str__(self):
        """
        String for representing the Model object.
        """
        return '%s' % (self.name)
