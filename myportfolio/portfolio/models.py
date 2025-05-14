from django.db import models

class ExpertiseLevel(models.TextChoices):
    BEGINNER = 'BEGINNER', 'Beginner'
    INTERMEDIATE = 'INTERMEDIATE', 'Intermediate'
    ADVANCED = 'ADVANCED', 'Advanced'
    EXPERT = 'EXPERT', 'Expert'

# Create your models here.

    
    
class Portfolio(models.Model):
    title = models.CharField(max_length=50)
    name = models.CharField(max_length=50, default='Md Ali Akbar')
    photo = models.ImageField(upload_to='images/', null=True, blank=True)
    intro = models.CharField(max_length=1000)
    resume = models.FileField(upload_to='resumes/', null=True, blank=True)
    mobile = models.CharField(max_length=50)
    email = models.CharField(max_length=50)
    linked_in = models.CharField(max_length=50)
    github = models.CharField(max_length=50)

    def __str__(self):
        return self.title
    
class Skill(models.Model):
    portfolio = models.ForeignKey(Portfolio, on_delete=models.CASCADE, related_name='skills')
    title = models.CharField(max_length=50)
    experties = models.CharField(max_length=20, choices=ExpertiseLevel.choices, default=ExpertiseLevel.BEGINNER)

    def __str__(self):
       return f"{self.title}"
    
class Project(models.Model):
    portfolio = models.ForeignKey(Portfolio, on_delete=models.CASCADE, related_name='projects')
    title = models.CharField(max_length=50)
    description = models.CharField(max_length=250)
    start_date = models.DateField()
    end_date = models.DateField(null=True, blank=True)
    client_name = models.CharField(max_length=50, null=True, blank=True)
    
    def __str__(self):
       return f"{self.title}"

class TechStack(models.Model):
    project = models.ForeignKey(Project, on_delete=models.CASCADE, null=True, blank=True, related_name='techstack')
    name = models.CharField(max_length=50)
    def __str__(self):
       return f"{self.name}"

class InterestedArea(models.Model):
    portfolio = models.ForeignKey(Portfolio, on_delete=models.CASCADE, related_name='interested_areas', null=True, blank=True)
    title = models.CharField(max_length=50)
    description = models.CharField(max_length=1000, null=True, blank=True)

    def __str__(self):
       return f"{self.title}"
    

class Achievement(models.Model):
    portfolio = models.ForeignKey(Portfolio, on_delete=models.CASCADE, related_name='achievements', null=True, blank=True)
    title = models.CharField(max_length=50)
    description = models.CharField(max_length=1000)

    def __str__(self):
       return f"{self.title}"
    
class Hobbies(models.Model):
    portfolio = models.ForeignKey(Portfolio, on_delete=models.CASCADE, related_name='hobbies', null=True, blank=True)
    title = models.CharField(max_length=50)
    description = models.CharField(max_length=1000, null=True, blank=True)

    def __str__(self):
       return f"{self.title}"

class Education(models.Model):
    portfolio = models.ForeignKey(Portfolio, on_delete=models.CASCADE, related_name='educations')
    course = models.CharField(max_length=50)
    intitution = models.CharField(max_length=50)
    start_date = models.DateField()
    end_date = models.DateField()
    score = models.CharField(max_length=10)
    
    def __str__(self):
       return f"{self.course}" 
    
class Experience(models.Model):
    portfolio = models.ForeignKey(Portfolio,on_delete=models.CASCADE, related_name='experience')
    name = models.CharField(max_length=50)
    designation = models.CharField(max_length=50)
    startd_date = models.DateField()
    end_date = models.DateField(null=True, blank=True)

    def __str__(self):
       return f"{self.name}" 
    