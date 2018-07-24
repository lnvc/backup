from django.urls import path, include
from django.conf.urls import url
from rest_framework import routers
from .views import QuestionViewSet, PersonViewSet, SubjectViewSet, QuestionSubjectViewSet, TestViewSet, TestQuestionViewSet, StudentViewSet, QuestionMakerViewSet, SchoolViewSet, AttendSchoolViewSet, CoachViewSet, CoachStudentViewSet, ParentViewSet, ParentStudentViewSet, TeamViewSet, StudentTeamViewSet, TestSubmissionViewSet, SubmissionViewSet
from . import views
#app_name = 'polls'
#urlpatterns = [
#	path('', views.IndexView.as_view(), name='index'),
#	path('<int:pk>/', views.DetailView.as_view(), name='detail'),
#	path('<int:pk>/results', views.ResultsView.as_view(), name='results'),
#	path('<int:question_id>/vote/', views.vote, name='vote'),
#]

router = routers.DefaultRouter()
router.register(r'questions', QuestionViewSet)
router.register(r'people', PersonViewSet)
router.register(r'subject', SubjectViewSet)
router.register(r'question-subject', QuestionSubjectViewSet)
router.register(r'test', TestViewSet)
router.register(r'test-question', TestQuestionViewSet)
router.register(r'student', StudentViewSet)
router.register(r'question-maker', QuestionMakerViewSet)
router.register(r'school', SchoolViewSet)
router.register(r'attend-school', AttendSchoolViewSet)
router.register(r'coach', CoachViewSet)
router.register(r'coach-student', CoachStudentViewSet)
router.register(r'parent', ParentViewSet)
router.register(r'parent-student', ParentStudentViewSet)
router.register(r'team', TeamViewSet)
router.register(r'student-team', StudentTeamViewSet)
router.register(r'test-submission', TestSubmissionViewSet)
router.register(r'submission', SubmissionViewSet)

urlpatterns = [
	url(r'^', include(router.urls)),
	url(r'^api-auth/', include('rest_framework.urls', namespace='rest_framework'))
]

