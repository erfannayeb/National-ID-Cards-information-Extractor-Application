from django.db import models


class Card(models.Model):
    first_name = models.CharField(max_length=100,null=True,blank=True)
    last_name  = models.CharField(max_length=100,null=True,blank=True)
    card_id = models.CharField(max_length=10,null=True,blank=True)
    father_name  = models.CharField(max_length=100,null=True,blank=True)
    birth_data = models.CharField(max_length=50,null=True,blank=True)
    expiration_data = models.CharField(max_length=50,null=True,blank=True)

    def __str__(self):
	    return self.card_id

