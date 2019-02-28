from django.db import models

class FormAuth(models.Model):
    Email = models.EmailField(null = False,blank = False)
    password = models.password
