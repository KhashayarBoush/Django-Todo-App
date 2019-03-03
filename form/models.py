from django.db import models

class List(models.Model):
    item = models.CharField(max_length = 300)
    compelet = models.BooleanField(default= False)

    def __str__(self):
        return self.item + ' | ' + str(self.compelet)

class Developer(models.Model):
    Name = models.CharField(max_length = 300)
    Family = models.CharField(max_length = 300)
    Email = models.EmailField(default = "khashayar.boush@programmer.net")
    Phone = models.IntegerField()
    
