from django.db import models

class Student(models.Model):
    name = models.CharField(max_length=100)
    date_of_birth = models.DateField()
    address = models.TextField()
    contact_number = models.CharField(max_length=15)
    email = models.EmailField()
    english_marks = models.IntegerField()
    physics_marks = models.IntegerField()
    chemistry_marks = models.IntegerField()
    
    def get_percentage(self):
        total_marks = self.english_marks + self.physics_marks + self.chemistry_marks
        return (total_marks / 300) * 100
    
    def __str__(self):
        return self.name