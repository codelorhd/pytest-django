from django.contrib import admin
from django.urls import path

from . import views

urlpatterns = [
    path('student/list/', views.StudentListAPIView.as_view(),
         name="student_list_api"),
    path('student/create/', views.StudentCreateAPIView.as_view(),
         name="student_create_api"),
    path('student/<int:pk>', views.StudentDetailAPIView.as_view(),
         name="student_detail_api"),
    path('student/<int:pk>/delete', views.StudentDeleteAPIView.as_view(),
         name="student_delete_api"),
    path('classroom/<int:capacity>', views.ClassRoomStudentCount.as_view(),
         name="classroom_student_capacity_api"),
]
