from django.db import models

# Create your models here.
from django.db.models import CASCADE


class ClientRegister_Model(models.Model):
    username = models.CharField(max_length=30)
    email = models.EmailField(max_length=30)
    password = models.CharField(max_length=10)
    phoneno = models.CharField(max_length=10)
    country = models.CharField(max_length=30)
    state = models.CharField(max_length=30)
    city = models.CharField(max_length=30)

class student_performance_model(models.Model):

    names= models.CharField(max_length=300)
    Enrollment_No= models.CharField(max_length=300)
    Gender= models.CharField(max_length=300)
    Contact_No= models.CharField(max_length=300)
    Course_Name= models.CharField(max_length=300)
    Degree_Name= models.CharField(max_length=300)
    College_Name= models.CharField(max_length=300)
    university_Name= models.CharField(max_length=300)
    Online_Course_Media= models.CharField(max_length=300)
    Conducted_Class= models.CharField(max_length=300)
    Attended_Class= models.CharField(max_length=300)
    Diagnostic_Assessments_Grade= models.IntegerField(max_length=300)
    Formative_Assessments_Grade= models.IntegerField(max_length=300)
    Interim_Assessments_Grade= models.IntegerField(max_length=300)
    Summative_Assessments_Grade= models.IntegerField(max_length=300)

class performance_ratio_model(models.Model):

     names = models.CharField(max_length=300)
     ENo = models.CharField(max_length=300)
     Gender = models.CharField(max_length=300)
     Course_Name = models.CharField(max_length=300)
     Degree_Name = models.CharField(max_length=300)
     College_Name = models.CharField(max_length=300)
     perfromance = models.CharField(max_length=300)


class review_Model(models.Model):
    uname = models.CharField(max_length=100)
    ureview = models.CharField(max_length=100)
    sanalysis = models.CharField(max_length=100)
    dt= models.CharField(max_length=300)
    tname= models.CharField(max_length=300)
    feedback = models.CharField(max_length=300)

class recommend_Model(models.Model):
    uname1 = models.CharField(max_length=100)
    pname = models.CharField(max_length=100)
    loc = models.CharField(max_length=100)
    dt= models.CharField(max_length=300)
    usefull= models.CharField(max_length=300)

class search_ratio_model(models.Model):
    names = models.CharField(max_length=300)
    ratio = models.CharField(max_length=300)



