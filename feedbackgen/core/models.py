from django.db import models

# Create your models here.
class User(models.Model):
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    email = models.EmailField(max_length=254)
    #not sure if this isn't covered by authentication
    # password = models.CharField(max_length=50)

    def __str__(self):
        return self.first_name

class Category(models.Model):
    name = models.CharField(max_length=100)
    description = models.CharField(max_length=500)

    def __str__(self):
        return self.name

class Template(models.Model):
    name = models.CharField(max_length=100)
    description = models.CharField(max_length=500)
    category = models.ForeignKey(Category, on_delete=models.CASCADE)

    def __str__(self):
        return self.name

class Userform(models.Model):
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    formName = models.CharField(max_length=100)
    description = models.CharField(max_length=500)
    templateChosen = models.ForeignKey(Template, on_delete=models.CASCADE)
    timeCreated = models.DateTimeField()

    def __str__(self):
        return self.formName

class FormData(models.Model):
    form = models.ForeignKey(Userform, on_delete=models.CASCADE)
    author = models.CharField(max_length=100)
    data = models.CharField(max_length=1000000)
    timeAdded = models.DateTimeField()