from django.urls import path

from api.views import TeacherListAPIView, TeacherCreateAPIView, TeacherUpdateAPIView, StudentDeleteAPIView, \
    StudentUpdateAPIView, StudentCreateAPIView, StudentListAPIView, TeacherDeleteAPIView

urlpatterns = [
    path('teachers/', TeacherListAPIView.as_view()),
    path('teachers/create/<int:pk>', TeacherCreateAPIView.as_view()),
    path('teachers/update/<int:pk>', TeacherUpdateAPIView.as_view()),
    path('teachers/delete/<int:pk>/', TeacherDeleteAPIView.as_view()),
    path('student/', StudentListAPIView.as_view()),
    path('student/create/<int:pk>/', StudentCreateAPIView.as_view()),
    path('student/update/<int:pk>/', StudentUpdateAPIView.as_view()),
    path('student/delete/<int:pk>/', StudentDeleteAPIView.as_view()),
]