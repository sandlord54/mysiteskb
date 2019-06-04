from userpr import models
from django.db import models
import datetime
import request



class Titempl(models.Model):
    namesobr = models.CharField('Имя собрания',max_length=70,unique=True)

    def __str__(self):
        return self.namesobr

class Vremidat (models.Model)    :
    datetime = models.DateTimeField(auto_now_add=False)  # дата и время

    #def __str__(self):
       # return self.datetime

class Moment (models.Model):
    nazv = models.CharField('nazv',max_length=100,db_index=True) #название собрания
    duration = models.TimeField(auto_now_add=False) #Продолжительность
    date = models.DateTimeField(auto_now_add=True)


    def __str__(self):
        return self.nazv

class Template(models.Model): #Шаблон собрания
    namet = models.CharField('namet',max_length=200)#название собрания
    theme = models.CharField('theme',max_length=250,db_index=True)#тема
    leading = models.CharField('lead',max_length=50) #Ведущий собрания. Т.К это шаблон здесь ведущего определит система.
    datetime = models.DateTimeField(auto_now_add=False)#дата

    def __str__(self):
        return self.namet


class Collect(models.Model):  # Собрание
    name = models.CharField('Название собрания', max_length=100, db_index=True,primary_key=True)
    data = models.DateTimeField(auto_now_add=False)
    tpesobr = models.CharField('Тип собрания',max_length= 20,default='Общедоступное')
    org = models.CharField('Организатор', max_length=70, unique=True)
    theme = models.CharField('Тема собрания', max_length=250)
    opisan = models.CharField('Описание собрания',max_length=500)
    #flagin = models.ForeignKey(Golos,on_delete=models.CASCADE,related_name='flagin')
    #peopleincoll = models.ForeignKey(Golos,on_delete=models.CASCADE,related_name='peopleincoll')

    def __str__(self):
        return self.name

class Golos(models.Model):
    namesobr = models.ForeignKey(Collect, default=False, on_delete=models.CASCADE, related_name='namesobr')
    username = models.ForeignKey('userpr.Userpr',verbose_name='Пользователь',related_name='up',on_delete=models.CASCADE,default=True)
    flag= models.BooleanField('flag',default=False)

class RequiredPeople(models.Model):
    namesobr = models.ManyToManyField(Titempl)
    listeners = models.ForeignKey('Collect',blank=True,on_delete=models.CASCADE,related_name='listeners')
    leading = models.ForeignKey(Collect,default=False,on_delete=models.CASCADE,related_name='leading')#
    #Ведущий должен взяться из СОБРАНИЯ.
    #С людьми которые будут на собрании, надо что-то придумать, где их можно хранить

   # def __str__(self):
       # return self.namesobr


class Peoplincollect (models.Model):
    nazvsobr = models.ForeignKey(Collect,default=False,on_delete=models.CASCADE,related_name='nazvsobr')
    user = models.ForeignKey('userpr.Userpr',verbose_name='user',on_delete=models.CASCADE,unique=False)
    #НЕ ПРАВИЛЬНО уникальность.

    #def __str__(self):
        #return self.nazvsobr, self.user






