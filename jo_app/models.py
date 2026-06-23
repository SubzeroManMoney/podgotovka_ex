# This is an auto-generated Django model module.
# You'll have to do the following manually to clean this up:
#   * Rearrange models' order
#   * Make sure each model has one field with primary_key=True
#   * Make sure each ForeignKey and OneToOneField has `on_delete` set to the desired behavior
#   * Remove `managed = False` lines if you wish to allow Django to create, modify, and delete the table
# Feel free to rename the models, but don't rename db_table values or field names.
from django.db import models


class Clients(models.Model):
    id = models.IntegerField(primary_key=True)
    secondname = models.CharField()
    firstname = models.CharField()
    phone = models.IntegerField()
    bday = models.DateField(blank=True, null=True)
    gender = models.IntegerField(blank=True, null=True)
    category = models.IntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'clients'


class Users(models.Model):
    id = models.IntegerField(primary_key=True)
    login = models.CharField()
    pass_field = models.CharField(db_column='pass')  # Field renamed because it was a Python reserved word.
    isadmin = models.BooleanField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'users'
