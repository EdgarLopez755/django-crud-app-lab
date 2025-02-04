from django.db import models
from django.urls import reverse



RATINGS = (
    ('A', 'Amazing'),
    ('O', 'Okay'),
    ('B', 'Bad')

)



# Create your models here.


class Park(models.Model):
    name = models.CharField(max_length=255)
    location = models.CharField(max_length=255)
    opening_date = models.DateField()
    description = models.TextField()

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse('park-detail', kwargs={'park_id': self.id})





class Ride(models.Model):
    
    date = models.DateField()
    rating = models.CharField(
        max_length=1,
        choices = RATINGS,
        default = RATINGS[0][0]
    )
    
    park = models.ForeignKey(Park, on_delete=models.CASCADE)

    def __str__(self):
        return f"{self.get_rating_display()} on {self.date}"

    