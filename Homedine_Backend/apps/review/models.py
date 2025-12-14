from django.db import models

class UserReview(models.Model):
    PROFESSION_CHOICES = [
        ('ENG' , 'Engineer'),
        ('DOC' , 'Doctor'),
        ('I.T' , 'Information Technologist'),
        ('LAW' , 'Lawyer'),
        ('ARC' , 'Architect'),
        ('ACC' , 'Accountant'),
        ('BUS' , 'Business Owner'),
        ('TEA' , 'Teacher'),
        ('LEC' , 'Lecturer'),
        ('DES' , 'Designer'),
        ('DEV' , 'Software Developer'),
        ('ANA' , 'Data Analyst'),
        ('SCI' , 'Scientist'),
        ('JOU' , 'Journalist'),
        ('MKT' , 'Marketing Specialist'),
        ('FIN' , 'Financial Analyst'),
        ('HRM' , 'Human Resource Manager'),
        ('ADM' , 'Administrator'),
        ('CON' , 'Consultant'),
        ('OTH' , 'Other'),
    ]

    Users_Full_Name = models.CharField(max_length=50)
    User_Profession = models.CharField(max_length=20, choices=PROFESSION_CHOICES, default='None')
    User_Review = models.TextField(blank=True, default='None, as such!')
    
    def __str__(self):
        return self.Users_Full_Name
    