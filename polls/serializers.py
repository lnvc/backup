from rest_framework import serializers
from . models import Question,  Person, Subject, Question_Subject, Test, Test_Question, Student, Question_Maker, School, Attend_School, Coach, Coach_Student, Parent, Parent_Student, Team, Student_Team, Test_Submission, Submission

class QuestionSerializer(serializers.ModelSerializer):
	class Meta:
		model = Question
		# fields=('question_text','pub_date',)
		fields= '__all__'
class PersonSerializer(serializers.ModelSerializer):
	class Meta:
		model = Person
		fields = '__all__'
class SubjectSerializer(serializers.ModelSerializer):
	class Meta:
		model = Subject
		fields = '__all__'
class QuestionSubjectSerializer(serializers.ModelSerializer):
        class Meta:
                model = Question_Subject
                fields = '__all__'

class TestSerializer(serializers.ModelSerializer):
	class Meta:
		model = Test
		fields = '__all__'

class TestQuestionSerializer(serializers.ModelSerializer):
	class Meta:
		model = Test_Question
		fields = '__all__'
class StudentSerializer(serializers.ModelSerializer):
	class Meta:
		model = Student
		fields = '__all__'
class QuestionMakerSerializer(serializers.ModelSerializer):
	class Meta:
		model=Question_Maker
		fields = '__all__'
class SchoolSerializer(serializers.ModelSerializer):
        class Meta:
                model=School
                fields = '__all__'
class AttendSchoolSerializer(serializers.ModelSerializer):
        class Meta:
                model=Attend_School
                fields = '__all__'
class CoachSerializer(serializers.ModelSerializer):
        class Meta:
                model=Coach
                fields = '__all__'
class CoachStudentSerializer(serializers.ModelSerializer):
        class Meta:
                model=Coach_Student 
                fields = '__all__'
class ParentSerializer(serializers.ModelSerializer):
        class Meta:
                model=Parent
                fields = '__all__'
class ParentStudentSerializer(serializers.ModelSerializer):
        class Meta:
                model=Parent_Student 
                fields = '__all__'
class TeamSerializer(serializers.ModelSerializer):
        class Meta:
                model=Team
                fields = '__all__'
class StudentTeamSerializer(serializers.ModelSerializer):
        class Meta:
                model=Student_Team 
                fields = '__all__'
class TestSubmissionSerializer(serializers.ModelSerializer):
        class Meta:
                model=Test_Submission
                fields = '__all__'

class SubmissionSerializer(serializers.ModelSerializer):
        class Meta:
                model=Submission
                fields = '__all__'


