from django.urls import path

from api.views import TeacherListAPIView

urlpatterns = [
    path('', TeacherListAPIView.as_view())
]