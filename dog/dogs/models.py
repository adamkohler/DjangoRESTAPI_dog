from django.db import models

from django.core.validators import MaxValueValidator, MinValueValidator

# Create your models here.
class Dog(models.Model):
    name = models.CharField(max_length=200)
    age = models.IntegerField()
    breed = models.ForeignKey(
        'Breed',
        related_name='breeds',
        on_delete=models.CASCADE) #models.CharField(max_length=200)
    gender = models.CharField(max_length=200)
    color = models.CharField(max_length=200)
    favoritefood = models.CharField(max_length=200)
    favoritetoy = models.CharField(max_length=200)
    
    def __str__(self):
        """A string representation of the model."""
        return self.name

class Breed(models.Model):    
    Tiny = 'tiny'
    Small = 'small'
    Medium = 'medium'
    Large = 'large'
    Size_Choices = (
        (Tiny, 'Tiny'),
        (Small, 'Small'),
        (Medium, 'Medium'),
        (Large, 'Large'),
    )
    name = models.CharField(max_length=200)
    size = models.CharField(
        max_length=6,
        choices=Size_Choices,
        default=Small,
    )#tiny, small, medium, large
    friendliness = models.IntegerField(default=3, validators=[MaxValueValidator(5), MinValueValidator(1)]) #1-5
    trainability = models.IntegerField(default=3, validators=[MaxValueValidator(5), MinValueValidator(1)]) #1-5
    sheddingamount = models.IntegerField(default=3, validators=[MaxValueValidator(5), MinValueValidator(1)]) #1-5
    exerciseneeds = models.IntegerField(default=3, validators=[MaxValueValidator(5), MinValueValidator(1)]) #1-5
        
    def __str__(self):
        """A string of the breed model."""
        return self.name
    