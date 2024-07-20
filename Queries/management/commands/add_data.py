from django.core.management.base import BaseCommand
from faker import Faker
from ...models import Doctor, Nurse, Patient, Hospital, MedicalRecord

class Command(BaseCommand):
    help = 'Populate the database with fake data'

    def handle(self, *args, **kwargs):
        fake = Faker()

        doctors = []
        for _ in range(10):
            doctor = Doctor.objects.create(
                name=fake.name(),
                specialization=fake.job(),
                contact_number=fake.phone_number()[:11]
            )
            doctors.append(doctor)

        nurses = []
        for _ in range(10):
            nurse = Nurse.objects.create(
                name=fake.name(),
                contact_number=fake.phone_number()[:11]
            )
            nurses.append(nurse)

        for _ in range(20):
            patient = Patient.objects.create(
                name=fake.name(),
                age=fake.random_int(min=1, max=100),
                nurse=fake.random_element(elements=nurses),
                date=fake.date_this_decade()
            )
            assigned_doctors = fake.random_elements(elements=doctors, length=fake.random_int(min=1, max=3))
            patient.doctor.set(assigned_doctors)

            hospital = Hospital.objects.create(
                patient=patient,
                nurse=patient.nurse
            )
            hospital.doctor.set(assigned_doctors)

            MedicalRecord.objects.create(
                patient=patient,
                diagnoses=fake.text(max_nb_chars=200),
                prescription=fake.text(max_nb_chars=200)
            )

