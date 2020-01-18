from django.db import models

# Create your models here.
from django.db import models
from auther.models import Author
class Book(models.Model):
    bname   =   models.CharField("book_name",max_length=50)
    bprice = models.FloatField("book_price")
    bauthor = models.CharField("book_author", max_length=50)
    bremarks = models.TextField("book_remarks", max_length=50)
    author = models.OneToOneField(Author,on_delete=models.CASCADE)

    class Meta:
        db_table='Book_Info'