from django.db import models

class Doctor(models.Model):
    name = models.CharField(max_length=50)
    specialization = models.CharField(max_length=50)
    contact_number = models.CharField(max_length=11)
    
class Nurse(models.Model):
    name = models.CharField(max_length=50)
    contact_number = models.CharField(max_length=11)
    
class Patient(models.Model):
    name = models.CharField(max_length=50)
    age = models.IntegerField()
    doctor = models.ManyToManyField(Doctor, related_name='patient_doctors')
    nurse = models.ForeignKey(Nurse, on_delete=models.CASCADE, related_name='patient_nurses')
    date = models.DateField(auto_now_add=True)
    
class Hospital(models.Model):
    patient = models.ForeignKey(Patient, on_delete=models.CASCADE, related_name='hospital_patients')
    doctor = models.ManyToManyField(Doctor, related_name='hospital_doctors')
    nurse = models.ForeignKey(Nurse, on_delete=models.CASCADE, related_name='hospital_nurses')
    
class MedicalRecord(models.Model):
    patient = models.ForeignKey(Patient, on_delete=models.CASCADE, related_name='record_patients')
    diagnoses = models.TextField()
    prescription = models.TextField()