from .models import Doctor, Nurse, Patient, Hospital, MedicalRecord
from django.db.models import Count, Sum, Avg, Max, Min, Q
from datetime import timedelta
from django.utils import timezone

# **Task 1**

# - Retrieve all patients admitted on a specific date.
Patient.objects.filter(date='2024-04-01').values()

# - Get the names of all doctors who have patients with a specific diagnosis.
MedicalRecord.objects.select_related('patient').filter(patient__doctor__diagnoses='Act as risk friend democratic hand base fund real office push security.').values('patient__doctor__name')

# - Find all patients treated by a particular nurse.
Patient.objects.select_related('nurse').filter(nurse__name='John Jacobs')

# - Retrieve the contact number of the doctor for a given patient.
Doctor.objects.prefetch_related('patient_doctors').filter(patient_doctors__name='Tyler Serrano').values('contact_number')

# - Get the total number of patients admitted to the hospital.
Hospital.objects.aggregate(Count('patient'))

# - Find the patients who are not assigned to any nurse.
Patient.objects.filter(nurse__isnull=True) 

# - Retrieve the names of nurses who have patients with a specific prescription.
MedicalRecord.objects.select_related('patient').filter(prescription='Property clear someone state participant hundred who recently worker trial history prove.').values('patient__nurse__name')

# - Get the average age of patients in the hospital.
Patient.objects.aggregate(Avg('age'))

# - Find the most recently admitted patient.
Patient.objects.order_by('date').last()

# - Retrieve all doctors who have more than five patients.
Patient.objects.annotate(num_patient = Count('doctor')).filter(num_patient__gte=6)
 
# - Find the patients who have been admitted for more than a week.
one_week = timezone.now().date() - timedelta(days=7)
Patient.objects.filter(date__lte=one_week).values()

# - Get the number of patients assigned to each nurse.
patient_nurse = Patient.objects.annotate(nurse_count=Count('nurse')).values('name', 'nurse_count')
for patient in patient_nurse:
  print(f'patient: {patient['name']},    nurses{patient['nurse_count']}')
  
# - Retrieve the names of patients who have a specific doctor.
Doctor.objects.prefetch_related('patient_doctors').filter(name='Jeremy Richardson').values('patient_doctors__name')

# - Find the doctors who specialize in a specific medical field.
Doctor.objects.filter(specialization='Recycling officer').values()

# - Get the names of patients treated by a doctor with a specific specialization.
Doctor.objects.prefetch_related('patient_doctors').filter(specialization='Recycling officer').values('patient_doctors__name')

# - Find the nurses who have not been assigned any patients.
Patient.objects.filter(nurse__isnull=True)

# - Retrieve the latest medical record for a given patient.
MedicalRecord.objects.select_related('patient').filter(patient__name='Barbara Robinson').latest('patient__date')

# - Get the names of patients with a specific diagnosis.
MedicalRecord.objects.select_related('patient').filter(diagnoses='Act as risk friend democratic hand base fund real office push security.').values('patient__name')    

# - Find the doctors who have patients of a certain age group.
Doctor.objects.prefetch_related('patient_doctors').filter(patient_doctors__age__gte=12, patient_doctors__age__lte=50)

# - Retrieve all patients with a specific prescription.
MedicalRecord.objects.select_related('patient').filter(prescription='Property clear someone state participant hundred who recently worker trial history prove.').values('patient')

# - Find the nurses who have patients with a specific age.
Patient.objects.select_related('nurse').filter(age__gte=12, age__lte=50).values('nurse') 

# - Get the total number of medical records in the system.
MedicalRecord.objects.count()

# - Retrieve the names of patients treated by a nurse with a specific contact number.
Patient.objects.select_related('nurse').filter(nurse__contact_number='7276154573').values("name") 

# - Find the patients who are treated by more than one doctor.
doctor_more = Patient.objects.annotate(doctor_count=Count('doctor')).values('name', 'doctor_count')
for patient in doctor_more:
  if patient['doctor_count'] > 1:
    print(f'patient: {patient['name']}')
    
# - Get the names of doctors who have treated patients with a specific prescription.
MedicalRecord.objects.select_related('patient').filter(prescription='Property clear someone state participant hundred who recently worker trial history prove.').values('patient__doctor__name')

# - Find the patients who have not been assigned to any doctor.
Patient.objects.filter(doctor__isnull=True)

# - Retrieve the doctors who have patients admitted on a specific date.
Doctor.objects.prefetch_related('patient_doctors').filter(patient_doctors__date='2024-07-17')
 
# - Get the number of patients admitted each month.
# - Find the patients with the highest age in the hospital.
Patient.objects.aggregate(Max('age'))

# - Retrieve all nurses who have patients admitted on a specific date.
Patient.objects.select_related('nurse').filter(date='2024-07-17').values('nurse')

# - Find the doctors who have patients with a specific age.
Doctor.objects.prefetch_related('patient_doctors').filter(patient_doctors__age=17) 

# - Get the number of patients treated by each doctor.
Doctor.objects.annotate(patient_count=Count('patient_doctors')).values()

# - Retrieve the names of patients with a specific age.
Patient.objects.filter(age=98).values('name')

# - Find the nurses who have patients with a specific diagnosis.
MedicalRecord.objects.select_related('patient').filter(diagnoses='Act as risk friend democratic hand base fund real office push security.').values('patient__nurse')

# - Get the names of patients treated by a nurse with a specific contact number.
Patient.objects.select_related('nurse').filter(nurse__contact_number='284-318-8704x759').values('name')

# - Find the doctors who have not been assigned any patients.
Patient.objects.filter(doctor__isnull=True).values('doctor')

# - Retrieve the patients who have medical records with a specific prescription.
MedicalRecord.objects.filter(prescription='Property clear someone state participant hundred who recently worker trial history prove.').values('patient')

# - Get the average age of patients treated by each doctor.
Doctor.objects.prefetch_related('patient_doctors').annotate(avg_age_patient=Avg('patient_doctors__age'))

# - Find the doctors who have patients with a specific prescription.
MedicalRecord.objects.filter(prescription='Property clear someone state participant hundred who recently worker trial history prove.').values('patient__doctor')

# - Retrieve the names of patients treated by a doctor with a specific contact number.
Patient.objects.filter(doctor__contact_number='284-318-8704x759').values('name') 

# - Find the nurses who have patients with a specific prescription.
MedicalRecord.objects.select_related('patient').filter(prescription='Property clear someone state participant hundred who recently worker trial history prove.').values('patient__nurse')

# - Get the total number of patients treated by nurses in a specific specialization.
specialization = Patient.objects.filter(doctor__specialization='Podiatrist')
Nurse.objects.filter(patient_nurses__in=specialization).annotate(patient_count=Count('patient_nurses'))

# - Retrieve the patients who have not been assigned to any nurse.
Patient.objects.filter(nurse__isnull=True)

# - Find the doctors who have patients admitted for more than a week.
Doctor.objects.prefetch_related('patient_doctors').filter(patient_doctors__date__lte=one_week)

# - Get the names of patients with a specific diagnosis treated by a specific doctor.
MedicalRecord.objects.select_related('patient').filter(Q(diagnoses='Act as risk friend democratic hand base fund real office push security.') & Q(patient__doctor__name='Zachary Green')).values('patient__name')

# - Find the nurses who have patients with a specific age group.
Nurse.objects.prefetch_related('patient_nurses').filter(patient_nurses__age__gte=12, patient_nurses__age__lte=50)

# - Retrieve the doctors who have patients with a specific diagnosis and age group.
MedicalRecord.objects.select_related('patient').filter(Q(diagnoses='Good employee not movement example develop local side.') & Q(patient__age__gte=12, patient__age__lte=50)).values('patient__doctor') 

# - Get the number of patients treated by each nurse in a specific specialization.   
specialization = Patient.objects.filter(doctor__specialization='Podiatrist')
Nurse.objects.filter(patient_nurses__in=specialization).annotate(patient_count=Count('patient_nurses'))
 
# - Find the patients who have been treated by more than one nurse.
nurse_more = Patient.objects.annotate(nurse_count=Count('nurse')).values('name', 'nurse_count')     
for patient in nurse_more:
  if patient['nurse_count'] > 1:
    patient(f'patient: {patient['name']},   nurse: {patient['nurse_count']}')
    
# - Retrieve the names of doctors who have patients with a specific diagnosis and age group.
MedicalRecord.objects.select_related('patient').filter(Q(diagnoses='Good employee not movement example develop local side.') & Q(patient__age__gte=12, patient__age__lte=50)).values('patient__doctor__name') 

# **Task 2**

# - Select all patients with their associated doctors and nurses.

Patient.objects.prefetch_related('patient_doctors').select_related('nurse').values('doctor', 'nurse')
Patient.objects.select_related('nurse', 'doctor').values('doctor', 'nurse')

# - Select all patients admitted after a specific date.
Patient.objects.filter(date__gte='2024-07-17')

# - Count the total number of patients.
Patient.objects.aggregate(Count('id'))

# - Count the total number of patients with a specific age.
Patient.objects.filter(age=14).count() 

# - Select all patients with their associated doctors and nurses prefetched.

Patient.objects.prefetch_related('doctor', 'nurse').values() 

# - Count the total number of doctors associated with each patient.
Patient.objects.annotate(doctor_count=Count('doctor')).values()

# - Sum the ages of all patients.
Patient.objects.aggregate(Sum('age'))

# - Select all patients along with the number of doctors associated with each.
Patient.objects.annotate(doctor_count=Count('doctor')).values('id', 'doctor_count')
  
# - Select all patients along with their medical records, if available.
Patient.objects.select_related('patient').values('id', 'record_patients')

# - Count the total number of nurses associated with each patient.
nurses = Patient.objects.annotate(nurse_count=Count('nurse')).values('id', 'nurse_count')
for patient in nurses:
  print(f'patient: {patient['name']},     nurse: {patient['nurse_count']}')
  
# - Select all patients with their associated nurses and the nurses' contact numbers.
Patient.objects.select_related('nurse').values('id', 'nurse', 'nurse__contact_number')  

# - Select all patients along with the total number of medical records for each.
patient_record = Patient.objects.annotate(total_count=Count('record_patients')).values('name', 'total_count')
for patient in patient_record:
  print(f'patient: {patient['name']},     medicalrecords: {patient['total_count']}')

# - Select all patients with their diagnoses and prescriptions, if available.
Patient.objects.select_related('patient').values('record_patients', 'record_patients__diagnoses', 'record_patients__prescription')

# - Count the total number of patients admitted in a specific year.
Patient.objects.annotate(count_patient=Count('id', filter=Q(date__year__in='2024')))

# - Select all patients along with their doctors' specializations.

Patient.objects.select_related('doctor').values('doctor__specialization')

# - Select all patients along with the count of medical records for each.
patient_record = Patient.objects.annotate(total_count=Count('record_patients')).values('name', 'total_count')
for patient in patient_record:
  print(f'patient: {patient['name']},     medicalrecords: {patient['total_count']}')
  
# - Select all doctors with the count of patients they are associated with.
Doctor.objects.prefetch_related('patient_doctors').annotate(patient_count=Count('patient_doctors'))

# - Select all patients along with the count of nurses they are associated with.
Patient.objects.select_related('nurse').annotate(nurse_count=Count('nurse')).values()

# - Annotate the average age of patients.
Patient.objects.annotate(avg_age=Avg('age')).values() 

# - Annotate the maximum age of patients.
Patient.objects.annotate(max_age=Max('age')).values() 

# - Annotate the minimum age of patients.
Patient.objects.annotate(min_age=Min('age')).values() 

# - Select all patients along with the earliest admission date.
Patient.objects.annotate(earliest_date = Min('date'))

# - Select all doctors with their associated patients prefetched.
doctors = Doctor.objects.prefetch_related('patient_doctors')
for doctor in doctors:
  print(doctor)
  for patient in doctor.patient_doctors.all():
    print(f'{patient}') 

# - Select all nurses with their associated patients prefetched.
nurses = Nurse.objects.prefetch_related('patient_nurses')
for nurse in nurses:
  for patient in nurse.patient_nurses.all():
    print(f'{nurse} ,       {patient}')

# - Select all patients along with the count of distinct doctors they are associated with.
Patient.objects.annotate(doctor_count=Count('doctor', distinct=True))