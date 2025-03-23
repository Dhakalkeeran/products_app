from django.db import models

# Create Models and define relationships

class Category(models.Model):
    name = models.CharField(max_length=50)
    
    def __str__(self):
        return self.name
    
class Tag(models.Model):
    name = models.CharField(max_length=50)
    
    def __str__(self):
        return self.name

class Product(models.Model):
    name = models.CharField(max_length=50)
    description = models.TextField()
    category = models.ForeignKey(Category, on_delete=models.CASCADE)    # assigning foreign key creates a column with foreign key id
    tags = models.ManyToManyField(Tag)                                  # product can have multiple tags
    
    def __str__(self):
        return self.name                                                # dunder method to modify str property