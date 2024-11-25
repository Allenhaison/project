from django.db import models



class Student(models.Model):
    student_id = models.CharField(max_length=10, unique=True)
    name = models.CharField(max_length=100)
    address = models.TextField()
    department = models.CharField(max_length=50)
    phone_number = models.CharField(max_length=15)
    photo = models.ImageField(upload_to='uploads/', default='uploads/default_photo.jpg')

    def __str__(self):
        return self.name
