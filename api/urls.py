from django.urls import path

from api.views import TeacherListAPIView, TeacherCreateAPIView, TeacherUpdateAPIView, StudentDeleteAPIView, \
    StudentUpdateAPIView, StudentCreateAPIView, StudentListAPIView, TeacherDeleteAPIView, VilAddressModelListAPIView, \
    VilAddressModelCreateAPIView, VilAddressModelUpdateAPIView, VilAddressModelDeleteAPIView, \
    TShAddressModelCreateAPIView, TShAddressModelUpdateAPIView, TShAddressModelDeleteAPIView, \
    TShAddressModelListAPIView, SchoolAddressModelListAPIView, SchoolAddressModelDeleteAPIView, \
    SchoolAddressModelUpdateAPIView, SchoolAddressModelCreateAPIView, ClassesModelCreateAPIView, \
    ClassesModelUpdateAPIView, ClassesModelDeleteAPIView, ClassesModeListAPIView, TakesModelListAPIView, \
    TakesModelCreateAPIView, TakesModelUpdateAPIView, TakesModelDeleteAPIView

urlpatterns = [
    path('teachers/', TeacherListAPIView.as_view()),
    path('teachers/create/', TeacherCreateAPIView.as_view()),
    path('teachers/update/<int:pk>/', TeacherUpdateAPIView.as_view()),
    path('teachers/delete/<int:pk>/', TeacherDeleteAPIView.as_view()),
    path('student/', StudentListAPIView.as_view()),
    path('student/create/<int:pk>/', StudentCreateAPIView.as_view()),
    path('student/update/<int:pk>/', StudentUpdateAPIView.as_view()),
    path('student/delete/<int:pk>/', StudentDeleteAPIView.as_view()),
    path('vil/', VilAddressModelListAPIView.as_view()),
    path('vil/create/', VilAddressModelCreateAPIView.as_view()),
    path('vil/update/<int:pk>/', VilAddressModelUpdateAPIView.as_view()),
    path('vil/delete/<int:pk>/', VilAddressModelDeleteAPIView.as_view()),

    path('tshaddress/', TShAddressModelListAPIView.as_view()),
    path('tshaddress/create/', TShAddressModelCreateAPIView.as_view()),
    path('tshaddress/update/<int:pk>/', TShAddressModelUpdateAPIView.as_view()),
    path('tshaddress/delete/<int:pk>/', TShAddressModelDeleteAPIView.as_view()),

    path('student/', SchoolAddressModelListAPIView.as_view()),
    path('student/create/', SchoolAddressModelCreateAPIView.as_view()),
    path('student/update/<int:pk>/', SchoolAddressModelUpdateAPIView.as_view()),
    path('student/delete/<int:pk>/', SchoolAddressModelDeleteAPIView.as_view()),




    path('class/', ClassesModeListAPIView.as_view()),
    path('class/create/', ClassesModelCreateAPIView.as_view()),
    path('class/update/<int:pk>/', ClassesModelUpdateAPIView.as_view()),
    path('class/delete/<int:pk>/', ClassesModelDeleteAPIView.as_view()),

    path('takes/', TakesModelListAPIView.as_view()),
    path('takes/create/', TakesModelCreateAPIView.as_view()),
    path('takes/update/<int:pk>/', TakesModelUpdateAPIView.as_view()),
    path('takes/delete/<int:pk>/', TakesModelDeleteAPIView.as_view()),



    path('student/', SchoolAddressModelListAPIView.as_view()),
    path('student/create/', SchoolAddressModelCreateAPIView.as_view()),
    path('student/update/<int:pk>/', SchoolAddressModelUpdateAPIView.as_view()),
    path('student/delete/<int:pk>/', SchoolAddressModelDeleteAPIView.as_view()),

    path('student/', SchoolAddressModelListAPIView.as_view()),
    path('student/create/', SchoolAddressModelCreateAPIView.as_view()),
    path('student/update/<int:pk>/', SchoolAddressModelUpdateAPIView.as_view()),
    path('student/delete/<int:pk>/', SchoolAddressModelDeleteAPIView.as_view()),

]