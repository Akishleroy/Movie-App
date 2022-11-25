from django.db import models
from django.urls import reverse 
from django.utils.text import slugify
from django.core.validators import MaxValueValidator,MinValueValidator

# Create your models here.

class Director(models.Model):
    first_name=models.CharField(max_length=100)
    last_name=models.CharField(max_length=100)
    director_email=models.EmailField()
    slug=models.SlugField(default='',null=False)
    # movie_set=models.ForeignKey(Movie,on_delete=models.CASCADE,null=True)

    def __str__(self):
        return f'{self.first_name} {self.last_name}'

    def save(self,*args,**kwargs):
        self.slug=slugify(self.first_name)
        super(Director,self).save(*args,**kwargs)

    def get_url(self):
        return reverse('director_number_slug', args=[self.slug])

class Actor(models.Model):
    slug=models.SlugField(default='',null=False)
    MALE='M'
    FEMALE='F'
    GENDER_CHOICES=[
        (MALE,'Male'),
        (FEMALE,'Female'),
    ]
    def save(self,*args,**kwargs):
        self.slug=slugify(self.first_name)
        super(Actor,self).save(*args,**kwargs)

    def get_url(self):
        return reverse('actor_number_slug', args=[self.slug])

    def __str__(self):
        return super().__str__()


    first_name=models.CharField(max_length=100)
    last_name=models.CharField(max_length=100)
    gender=models.CharField(max_length=7,choices=GENDER_CHOICES,default=MALE)

    def __str__(self):
        if self.gender==self.MALE:
            return f'Актёр - {self.first_name} {self.last_name}'
        if self.gender==self.FEMALE:
            return f'Актриса - {self.first_name} {self.last_name}'




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
    director=models.ForeignKey(Director,on_delete=models.CASCADE,null=True)
    actors=models.ManyToManyField(Actor)

    def save(self,*args,**kwargs):
        self.slug=slugify(self.name)
        super(Movie,self).save(*args,**kwargs)

    def __str__(self):
        return f'{self.name}-{self.rating}%'

    def get_url(self):
        return reverse('movie_number', args=[self.slug])