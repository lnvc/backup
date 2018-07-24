from django.http import HttpResponseRedirect
from django.shortcuts import get_object_or_404, render
from django.urls import reverse
from django.views import generic
from django.utils import timezone
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status, viewsets, generics
from . serializers import QuestionSerializer, PersonSerializer, SubjectSerializer, QuestionSubjectSerializer, TestSerializer, TestQuestionSerializer, StudentSerializer, QuestionMakerSerializer, SchoolSerializer, AttendSchoolSerializer, CoachSerializer, CoachStudentSerializer, ParentSerializer, ParentStudentSerializer, TeamSerializer, StudentTeamSerializer, TestSubmissionSerializer, SubmissionSerializer
from rest_framework.parsers import MultiPartParser, FormParser, JSONParser

from .models import Question, Person, Subject, Question_Subject, Test, Test_Question, Student, Question_Maker, School, Attend_School, Coach, Coach_Student, Parent, Parent_Student, Team, Student_Team, Test_Submission, Submission

# def index(request):
# 	latest_question_list = Question.objects.order_by('-pub_date')[:5]
# 	context = {'latest_question_list': latest_question_list	}
# 	return render(request, 'polls/index.html', context)

# def detail(request, question_id):
# 	question = get_object_or_404(Question, pk=question_id)
# 	return render(request, 'polls/detail.html', {'question': question})

# def results(request, question_id):
# 	result = get_object_or_404(Question, pk=question_id)
# 	return render(request, 'polls/results.html', {'result': result})
class PersonViewSet(viewsets.ModelViewSet):
	queryset=Person.objects.all()
	serializer_class=PersonSerializer
class QuestionViewSet(viewsets.ModelViewSet):
	parser_classes = (MultiPartParser, FormParser, JSONParser, )
	queryset=Question.objects.all()
	serializer_class = QuestionSerializer
class SubjectViewSet(viewsets.ModelViewSet):
	parser_classes = (MultiPartParser, FormParser, JSONParser, )
	queryset=Subject.objects.all()
	serializer_class = SubjectSerializer
class QuestionSubjectViewSet(viewsets.ModelViewSet):
	parser_classes = (MultiPartParser, FormParser, JSONParser, )
	queryset = Question_Subject.objects.all()
	serializer_class = QuestionSubjectSerializer
class TestViewSet(viewsets.ModelViewSet):
	parser_classes = (MultiPartParser, FormParser, JSONParser, )
	queryset = Test.objects.all()
	serializer_class = TestSerializer
class TestQuestionViewSet(viewsets.ModelViewSet):
	parser_classes = (MultiPartParser, FormParser, JSONParser, )
	queryset = Test_Question.objects.all()
	serializer_class = TestQuestionSerializer
class StudentViewSet(viewsets.ModelViewSet):
	parser_classes = (MultiPartParser, FormParser, JSONParser, )
	queryset = Student.objects.all()
	serializer_class = StudentSerializer
class QuestionMakerViewSet(viewsets.ModelViewSet):
	parser_classes = (MultiPartParser, FormParser, JSONParser, )
	queryset = Question_Maker.objects.all()
	serializer_class = QuestionMakerSerializer
class SchoolViewSet(viewsets.ModelViewSet):
	parser_classes = (MultiPartParser, FormParser, JSONParser, )
	queryset=School.objects.all()
	serializer_class = SchoolSerializer
class AttendSchoolViewSet(viewsets.ModelViewSet):
        parser_classes = (MultiPartParser, FormParser, JSONParser, )
        queryset=Attend_School.objects.all()
        serializer_class = AttendSchoolSerializer
class CoachViewSet(viewsets.ModelViewSet):
	parser_classes = (MultiPartParser, FormParser, JSONParser, )
	queryset = Coach.objects.all()
	serializer_class = CoachSerializer
class CoachStudentViewSet(viewsets.ModelViewSet):
	parser_classes = (MultiPartParser, FormParser, JSONParser, )
	queryset = Coach_Student.objects.all()
	serializer_class = CoachStudentSerializer
class ParentViewSet(viewsets.ModelViewSet):
        parser_classes = (MultiPartParser, FormParser, JSONParser, )
        queryset = Parent.objects.all()
        serializer_class = ParentSerializer
class ParentStudentViewSet(viewsets.ModelViewSet):
        parser_classes = (MultiPartParser, FormParser, JSONParser, )
        queryset = Parent_Student.objects.all()
        serializer_class = ParentStudentSerializer
class TeamViewSet(viewsets.ModelViewSet):
        parser_classes = (MultiPartParser, FormParser, JSONParser, )
        queryset = Team.objects.all()
        serializer_class = TeamSerializer
class StudentTeamViewSet(viewsets.ModelViewSet):
        parser_classes = (MultiPartParser, FormParser, JSONParser, )
        queryset = Student_Team.objects.all()
        serializer_class = StudentTeamSerializer
class TestSubmissionViewSet(viewsets.ModelViewSet):
        parser_classes = (MultiPartParser, FormParser, JSONParser, )
        queryset = Test_Submission.objects.all()
        serializer_class = TestSubmissionSerializer
class SubmissionViewSet(viewsets.ModelViewSet):
        parser_classes = (MultiPartParser, FormParser, JSONParser, )
        queryset = Submission.objects.all()
        serializer_class = SubmissionSerializer


class QuestionList(APIView):
	def get(self,request):
		q = Question.objects.all()
		serializer = QuestionSerializer(q, many=False)
		return Response(serializer.data)

	def post(self,request):
		serializer = QuestionSerializer(data=request.data)
		if serializer.is_valid():
			serializer.save()
			return Response(serializer.data, status=status.HTTP_201_CREATED)
		return Response(serializer.errors, status = status.HTTP_400_BAD_REQUEST)
 
class IndexView(generic.ListView):
	template_name='polls/index.html'
	context_object_name='latest_question_list'

	def get_queryset(self):
		"""Return the last five published quesions
		not including those set to be published in
		the future)."""
		return Question[:5]

class DetailView(generic.DetailView):
	model=Question
	template_name='polls/detail.html'
	def get_queryset(self):
		return Question.objects.filter(pub_date__lte=timezone.now())

class ResultsView(generic.DetailView):
	model=Question
	template_name='polls/results.html'

