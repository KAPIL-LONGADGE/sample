from django.db import models

# Create your models here.
from django.db import models

# Create your models here.

class Author(models.Model):
    aname  =   models.CharField("author_name",max_length=50)
    aage = models.IntegerField("author_age")
    aexp = models.CharField("author_exp", max_length=50)
    aemail=models.EmailField("author_email",max_length=50)
    class Meta:
        db_table='Author_Info'