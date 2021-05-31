from django.db import models


# Create your models here.

class MultipleDatabaseApp(models.Model):
    title=models.CharField(max_length=50)
    content=models.CharField(max_length=50)
    app_name=models.CharField(max_length=50)

    def __str__(self):
        return self.title