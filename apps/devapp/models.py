from django.db import models
from django.urls import reverse

# Create your models here.

class Categories(models.Model):
    categoryname = models.CharField(max_length=50)

    def __str__(self):
        return self.categoryname
        
class Codes(models.Model):
    code = models.CharField(max_length=10)
    endesc = models.CharField(max_length=100)
    remarks = models.CharField(max_length=100,blank=True, null=True)
    ardesc = models.CharField(max_length=100)
    category = models.ForeignKey(Categories, on_delete=models.CASCADE)

    def __str__(self):
        html = '<div class="container"><div class="row"><div class="col">'
        html =  html +  self.code 
        html =  html + '</div><div class="col">'
        html =  html + self.endesc
        html =  html + '</div><div class="col">'
        html =  html + self.ardesc
        html =  html + '</div></div></div>'
        #return self.code + " - " + self.endesc + " - " + self.ardesc
        return html

    def get_absolute_url(self):
        return reverse('create-codes')

#***********************************************************************************************************************

class CategoriesModel(models.Model):
    categoryname = models.CharField(max_length=50)

    def __str__(self):
        return self.categoryname
        
class CodesModel(models.Model):
    code = models.CharField(max_length=10)
    endesc = models.CharField(max_length=100)
    remarks = models.CharField(max_length=100,blank=True, null=True)
    ardesc = models.CharField(max_length=100)

    mytest = models.ForeignKey(
        'self',
        models.CASCADE,
        null=True,blank=True,
        related_name='related_models'
    )

    category = models.ForeignKey(CategoriesModel, on_delete=models.CASCADE,null=True, blank=True,related_name='Categories',related_query_name='Category')

    def __str__(self):
        html = '<div class="container"><div class="row"><div class="col">'
        html =  html +  self.code 
        html =  html + '</div><div class="col">'
        html =  html + self.endesc
        html =  html + '</div><div class="col">'
        html =  html + self.ardesc
        html =  html + '</div></div></div>'
        #return self.code + " - " + self.endesc + " - " + self.ardesc
        return html

    def get_absolute_url(self):
        return reverse('create-codes')

# Date
# Type
# RelatedIssues1
# RelatedIssues2
# RelatedIssues3
# Project
# Remarks
# Status
class GenerateModel(models.Model):
    datepart = models.DateField()
    thetype = models.ForeignKey('self', on_delete=models.CASCADE,null=True,blank=True,related_name='thetype_related_models')
    relatedIssues1 = models.ForeignKey('self', on_delete=models.CASCADE,null=True,blank=True,related_name='relatedIssues1_related_models')
    relatedIssues2 = models.ForeignKey('self', on_delete=models.CASCADE,null=True,blank=True,related_name='relatedIssues2_related_models')
    relatedIssues3 = models.ForeignKey('self', on_delete=models.CASCADE,null=True,blank=True,related_name='relatedIssues3_related_models')
    project = models.ForeignKey('self', on_delete=models.CASCADE,null=True,blank=True,related_name='Project_related_models')
    remarks = models.CharField(max_length=100,blank=True, null=True)
    status = models.ForeignKey('self', on_delete=models.CASCADE,null=True,blank=True,related_name='Remarks_related_models')


    def __str__(self):
        return self.datepart #+ " - " + self.endesc + " - " + self.ardesc