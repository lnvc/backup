import datetime
from django.contrib.postgres.fields import ArrayField
from django.db import models
from django.utils import timezone

class Person(models.Model):
	name = models.CharField(max_length=200)
	age = models.IntegerField(default=0)
class Question_Maker(models.Model):
        username = models.CharField(max_length=250)
        email = models.EmailField()
        password = models.CharField(max_length=250)
class Question(models.Model):
	problem_statement = models.CharField(max_length=1000,blank=True)
	question_maker = models.ForeignKey(Question_Maker, on_delete=models.SET_NULL, blank=True, null=True)
	choice_a = models.CharField(max_length=1000, blank=True)
	choice_b = models.CharField(max_length=1000,blank=True)
	choice_c = models.CharField(max_length=1000,blank=True)
	choice_d = models.CharField(max_length=1000,blank=True)
	CHOICES = (
		('A', 'A'),
		('B', 'B'),
		('C', 'C'),
		('D', 'D'),
	)
	GRADES = (
		('1','1'),
		('2','2'),
		('3','3'),
		('4','4'),
		('5','5'),
		('6','6'),
		('7','7'),
		('8','8'),
		('9','9'),
		('10','10'),
		('11','11'),
	)
	answer = models.CharField(max_length=1,choices=CHOICES,default='A')
	grade_level = models.CharField(max_length=1,choices=GRADES,default='1')
	time_limit = models.IntegerField(default=15)
	tips = ArrayField(models.CharField(max_length=1000,blank=True),null=True, blank=True)
	equation = models.CharField(max_length=1000,blank=True)
	solution = models.CharField(max_length=1000,blank=True)
	image_question = models.ImageField(upload_to='media/images/',blank=True,null=True)
	image_equation = models.ImageField(upload_to='media/images/',blank=True,null=True)
	image_solution = models.ImageField(upload_to='media/images/',blank=True,null=True)
	def __str__(self):
		return self.problem_statement
class Subject(models.Model):
	category_name = models.CharField(max_length=1000,null=True,blank=True)

class Question_Subject(models.Model):
	question = models.ForeignKey(Question, on_delete=models.CASCADE)
	subject = models.ForeignKey(Subject, on_delete=models.CASCADE)
	date_added = models.DateField(auto_now_add=True)
	date_updated = models.DateField(auto_now=True)
class Test(models.Model):
	test_name = models.CharField(max_length=1000)
	GRADES = (
                ('1','1'),
                ('2','2'),
                ('3','3'),
                ('4','4'),
                ('5','5'),
                ('6','6'),
                ('7','7'),
                ('8','8'),
                ('9','9'),
                ('10','10'),
                ('11','11'),
        )
	TYPES = (
		('F', 'Finals'),
		('E', 'Elims'),
		('P', 'Practice'),
		('T', 'Team'),
	)
	grade_level = models.CharField(max_length=1, choices=GRADES, default='1')
	test_type = models.CharField(max_length=1, choices=TYPES, default='P')
	
class Test_Question(models.Model):
	test = models.ForeignKey(Test, on_delete=models.CASCADE)
	question = models.ForeignKey(Question, on_delete=models.CASCADE)
	is_current_question = models.BooleanField()
	date_added = models.DateField(auto_now_add=True)
	date_updated = models.DateField(auto_now=True)
class Student(models.Model):
	email = models.EmailField(max_length=1000)
	name = models.CharField(max_length=1000)
	GRADES = (
                ('1','1'),
                ('2','2'),
                ('3','3'),
                ('4','4'),
                ('5','5'),
                ('6','6'),
                ('7','7'),
                ('8','8'),
                ('9','9'),
                ('10','10'),
                ('11','11'),
        )
	grade_level = models.CharField(max_length=1, choices=GRADES)
	username = models.CharField(max_length=1000)
	password = models.CharField(max_length=1000)
	awards = ArrayField(models.CharField(max_length=250),blank=True,null=True)

class School(models.Model):
	school_name = models.CharField(max_length=250)
	region = models.CharField(max_length=250)
class Attend_School(models.Model):
	school = models.ForeignKey(School, on_delete=models.CASCADE)
	student = models.ForeignKey(Student, on_delete=models.CASCADE)
	currently_attending = models.BooleanField()
	student_awards = ArrayField(models.CharField(max_length=250),blank=True,null=True)
class Coach(models.Model):
	username = models.CharField(max_length=1000)
	password = models.CharField(max_length=1000)
	email = models.EmailField(max_length=250)
class Coach_Student(models.Model):
	student = models.ForeignKey(Student, on_delete=models.CASCADE)
	coach = models.ForeignKey(Coach, on_delete=models.CASCADE)
	is_current_coach = models.BooleanField()
class Parent(models.Model):
        username = models.CharField(max_length=1000)
        password = models.CharField(max_length=1000)
        email = models.EmailField(max_length=250)
class Parent_Student(models.Model):
        student = models.ForeignKey(Student, on_delete=models.CASCADE)
        parent = models.ForeignKey(Parent, on_delete=models.CASCADE)

class Team(models.Model):
	team_name = models.CharField(max_length=1000)
	date_created = models.DateField(auto_now_add=True)
	date_updated = models.DateField(auto_now=True)
class Student_Team(models.Model):
	student = models.ForeignKey(Student, on_delete=models.CASCADE)
	team = models.ForeignKey(Team, on_delete=models.CASCADE)
	is_current_member = models.BooleanField()
	date_joined = models.DateField(auto_now_add=True)
	date_updated = models.DateField(auto_now=True)
class Test_Submission(models.Model):
	TYPES = (
                ('F', 'Finals'),
                ('E', 'Elims'),
                ('P', 'Practice'),
                ('T', 'Team'),
        )
	submission_type=models.CharField(max_length=1, choices=TYPES, default='P')
	student = models.ForeignKey(Student, on_delete=models.SET_NULL, blank=True, null=True)
	test = models.ForeignKey(Test, on_delete=models.SET_NULL, blank=True, null=True)
	points = models.IntegerField(default=1)
	datetime_submitted = models.DateTimeField(auto_now_add=True)
	elapsed_time = models.IntegerField(default=1)
class Submission(models.Model):
	test_submission = models.ForeignKey(Test_Submission, on_delete=models.CASCADE)
	TYPES = (
                ('F', 'Finals'),
                ('E', 'Elims'),
                ('P', 'Practice'),
                ('T', 'Team'),
        )
	submission_type = models.CharField(max_length=1, choices=TYPES, default='P')
	student = models.ForeignKey(Student, on_delete=models.CASCADE)
	test = models.ForeignKey(Test, on_delete=models.SET_NULL, null=True)
	question = models.ForeignKey(Test_Question, on_delete=models.SET_NULL, null=True)
	submitted_answer = models.CharField(max_length=1)
	is_correct = models.BooleanField()
	datetime_submitted = models.DateTimeField(auto_now_add=True)
	elapsed_time = models.IntegerField()
