from django.db import models


class Category(models.Model):
        name=models.CharField(max_length=100)
        img=models.ImageField(upload_to="pic")

class Products(models.Model):
        pro=models.ForeignKey(Category,related_name="category",on_delete=models.CASCADE)
        name=models.CharField(max_length=100)
        img=models.ImageField(upload_to="pic")
        desc=models.TextField()
        qty=models.IntegerField()
        discount=models.IntegerField(default=0)
        price=models.IntegerField()
        date=models.DateTimeField(auto_now_add=True)







