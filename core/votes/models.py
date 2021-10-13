
from django.contrib.auth.models import User
from django.db import models
from django.db.models.fields import BooleanField


# category.
class category(models.Model):
    type=models.CharField(max_length=100)

    def __str__(self):
        return self.type 

# yes_opine y no opine
class votesModel(models.Model):
    user_create=models.ForeignKey(User,on_delete=models.CASCADE)
    title=models.CharField(max_length=100,null=False)
    body=models.TextField(null=False)
    yes_opine=models.ManyToManyField(User,blank=True,related_name='yes')
    No_opine=models.ManyToManyField(User,blank=True,related_name='no')
    categorys=models.ManyToManyField(category,blank=False,related_name='category')
    isclosed=BooleanField(default=False)

    class Meta:
        ordering = ['-id']

    def __str__(self):
        return self.title 



