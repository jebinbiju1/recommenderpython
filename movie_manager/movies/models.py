from django.db import models

class Category(models.Model):
    name=models.CharField(max_length=200)

    def __str__(self):
        return self.name

class MovieInfo(models.Model):
    title=models.CharField(max_length=250)
    poster=models.ImageField(upload_to='poster',null=True)
    release_date=models.DateField(null=True)
    description=models.TextField(blank=True)
    category=models.ForeignKey(Category,null=True,on_delete=models.CASCADE)
    actors=models.CharField(max_length=250,null=True)
    trailer_link=models.CharField(max_length=100)


    def __str__(self):
        return self.title

