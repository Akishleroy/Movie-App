from django.db import models
from django.urls import reverse 
from django.utils.text import slugify
from django.core.validators import MaxValueValidator,MinValueValidator

# Create your models here.

class Movie(models.Model):
    EUR='E'
    DOL='D'
    RUB='R'
    CURRENCY_CHOICES=[
        (DOL,'Dollars'),
        (RUB,'Rubles'),
        (EUR,'Euro'),
    ]

    name = models.CharField(max_length=40)
    rating=models.IntegerField(validators=[MinValueValidator(1),MaxValueValidator(100)])
    year=models.IntegerField(null=True,blank=True)
    budget=models.IntegerField(default=1000000,validators=[MinValueValidator(1)])
    slug=models.SlugField(default='',null=False)
    currency=models.CharField(max_length=3,choices=CURRENCY_CHOICES,default=RUB)

    def save(self,*args,**kwargs):
        self.slug=slugify(self.name)
        super(Movie,self).save(*args,**kwargs)

    def __str__(self):
        return f'{self.name}-{self.rating}%'

    def get_url(self):
        return reverse('movie_number', args=[self.slug])