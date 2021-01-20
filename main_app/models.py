from django.db import models

# Create your models here.

class car(models.Model):
    name = models.CharField(max_length = 20)
    company = models.CharField(max_length = 20)
    c_id = models.AutoField(primary_key=True)
    cost = models.IntegerField()

    def __str__(self):
        return self.name
    

class review(models.Model):
    car_model = models.ForeignKey(car, on_delete = models.CASCADE)
    name = models.CharField(max_length = 20)
    rates = (('1','1'),
            ('2','2'),
            ('3','3'),
            ('4','4'),
            ('5','5'))
    r_id = models.AutoField(primary_key=True)
    rating = models.CharField(max_length = 1, choices=rates, default='1') 
    description = models.CharField(max_length = 300)

