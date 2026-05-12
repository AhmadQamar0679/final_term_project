from django.db import models
from django.contrib.auth.models import User
from django.utils import timezone


# ─────────────────────────────────────────
#  PATIENT MODEL
# ─────────────────────────────────────────
class Patient(models.Model):
    GENDER_CHOICES = [
        ('M', 'Male'),
        ('F', 'Female'),
        ('O', 'Other'),
    ]

    user         = models.ForeignKey(User, on_delete=models.SET_NULL, null=True, blank=True)
    patient_name = models.CharField(max_length=100)
    patient_age  = models.IntegerField(blank=True, null=True)
    gender       = models.CharField(max_length=1, choices=GENDER_CHOICES)
    contact      = models.CharField(max_length=11)        # ✅ Fixed typo: 'contect' → 'contact'
    address      = models.TextField(blank=True, null=True)
    time         = models.DateTimeField(default=timezone.now)

    def __str__(self):
        return self.patient_name

    class Meta:
        ordering = ['-time']
        verbose_name        = 'Patient'
        verbose_name_plural = 'Patients'


# ─────────────────────────────────────────
#  MEDICINE MODEL
# ─────────────────────────────────────────
class Medicine(models.Model):
    name        = models.CharField(max_length=100)
    description = models.TextField(blank=True, null=True)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name_plural = 'Medicines'


# ─────────────────────────────────────────
#  PRESCRIPTION MODEL
# ─────────────────────────────────────────
class Prescription(models.Model):
    medicine     = models.ForeignKey(Medicine, on_delete=models.CASCADE)
    dosage       = models.CharField(max_length=100)    # e.g. "2 tablets per day"
    duration     = models.CharField(max_length=50)     # e.g. "7 days"
    instructions = models.TextField(blank=True, null=True)  # e.g. "Take after meal"

    def __str__(self):
        return f"{self.medicine.name} - {self.dosage}"


# ─────────────────────────────────────────
#  CHECKUP HISTORY MODEL
# ─────────────────────────────────────────
class Checkup_history(models.Model):
    # ✅ Linked to Patient
    patient      = models.ForeignKey(Patient, on_delete=models.CASCADE, null=True, blank=True)

    # ✅ Linked to Prescription
    prescription = models.ForeignKey(Prescription, on_delete=models.SET_NULL, null=True, blank=True)

    doctor_name  = models.CharField(max_length=100)
    temperature  = models.FloatField()                 # ✅ Float is better for temperature (e.g. 98.6)
    blood_pressure = models.CharField(max_length=20, blank=True, null=True)  # e.g. "120/80"
    weight       = models.FloatField(blank=True, null=True)   # in kg
    notes        = models.TextField(blank=True, null=True)
    checkup_date = models.DateTimeField(default=timezone.now) # ✅ Added date tracking

    def __str__(self):
        return f"{self.patient} - Dr.{self.doctor_name} ({self.checkup_date.strftime('%Y-%m-%d')})"

    class Meta:
        ordering            = ['-checkup_date']
        verbose_name        = 'Checkup History'
        verbose_name_plural = 'Checkup Histories'