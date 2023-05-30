from unicodedata import name
from django.urls import path
from OTS.views import *
urlpatterns = [
    path('',ots,name='home'),
    path('new-question',newQuestion,name='newquestion'),
    path('view-questions',viewQuestions, name='viewquestions'),
    path('save-question',saveQuestion ,name='savequestion'),
    path('edit-question',editQuestion ,name='editquestion'),
    path('edit-save-question',editSaveQuestion ,name='editsavequestion'),
    path('delete-question',deleteQuestion ,name='deletequestion'),
    path('signup',signup ,name='signup'),
    path('check-name',checkUser,name='checkuser'),
    path('save-user',saveUser ,name='saveuser'),
    path('login',login ,name='login'),
    path('login-validation',loginValidation ,name='loginvalidation'),
    path('logout',logout ,name='logout'),
    path('start-test',startTest ,name='starttest'),
    path('submit-test',submitTest ,name='submittest'),
    path('user-results',userResults , name='userresults'),
]
