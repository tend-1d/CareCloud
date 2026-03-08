from django.db import models

# Create your models here.

class Patient( models.Model ):
    firstname = models.CharField(max_length=200)
    lastname = models.CharField(max_length=50)
    dob = models.DateField()
    age = models.IntegerField()
    gender = models.CharField(max_length=20)
    dateregistered = models.DateTimeField(auto_now_add=True)
    medicalhistory =models.TextField()

    def __str__ (self) :
        return self.firstname + " " + self.lastname

class Doctor( models.Model ):
    firstname = models.CharField(max_length=200)
    lastname = models.CharField(max_length=50)
    dob = models.DateField(null=True,blank=True)
    nationality = models.CharField(max_length=50)
    age = models.IntegerField ()
    gender = models.CharField(max_length=20)
    phonenumber = models.IntegerField()
    email = models.EmailField ()
    medicallicencenumber = models.IntegerField()
    specialization = models.CharField (max_length=50)

    def __str__(self):
        return self.firstname + " " + self.lastname

class MyAppointments(models.Model):
    name = models.CharField(max_length=200)
    email = models.EmailField()
    phone = models.CharField(max_length=20)
    datetime = models.DateTimeField(auto_now_add=True)
    department = models.CharField(max_length=100)
    doctor = models.CharField(max_length=100)
    message = models.TextField()

    def __str__(self):
        return self.name

class ContactMessage(models.Model):
    name = models.CharField(max_length=200)
    email = models.EmailField()
    subject = models.CharField(max_length=200)
    message = models.TextField()

    def __str__(self):
        return self.name
    

class Transaction(models.Model):
    phone_number = models.CharField(max_length=15)
    amount = models.DecimalField(max_digits=10, decimal_places=2)
    transaction_id = models.CharField(max_length=100, unique=True)
    status = models.CharField(max_length=20, choices=[('Success', 'Success'), ('Failed', 'Failed')])
    date = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.phone_number} - {self.amount} - {self.status}"  


    

