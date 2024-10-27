from faker import Faker
import random
from .models import *
fake = Faker()


def create_subject_marks():
    try:
        student_objs = Student.objects.all()
        for student in student_objs:
            subjects = Subject.objects.all()
            for subject in subjects:
                # Check if a SubjectMarks entry already exists for this student and subject
                if not SubjectMarks.objects.filter(subject=subject, student=student).exists():
                    SubjectMarks.objects.create(
                        subject=subject,
                        student=student,
                        marks=random.randint(0, 100),
                    )
        print("Subject marks created successfully for each student.")

    except Exception as e:
        print("Error creating subject marks:", e)
        



def seed_db(n=10) -> None:
    try:
        # Ensure departments exist before creating student records
        departments_objs = Department.objects.all()
        if not departments_objs.exists():
            print("No departments found. Please add departments before seeding students.")
            return
        
        for _ in range(n):
            # Select a random department
            department = random.choice(departments_objs)
            
            # Generate a unique student ID
            while True:
                student_id = f"stu-0{random.randint(100,999)}"
                if not StudentID.objects.filter(student_id=student_id).exists():
                    break
            
            student_id_obj = StudentID.objects.create(student_id = student_id)    
                    
            student_name = fake.name()
            student_email = fake.email()
            student_age = random.randint(18,30)
            student_address = fake.address()
  

            Student.objects.create(
                department = department,
                student_id = student_id_obj,
                student_name = student_name,
                student_email = student_email,
                student_age = student_age,
                student_address = student_address,
            )
            
            print(f"{n} student records seeded successfully.")
            
    except Exception as e:
        print(e)