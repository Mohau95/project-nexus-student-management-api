from django.urls import path

from students.views import StudentRetrieveUpdateDeleteView, StudentListCreateView

urlpatterns = [
    path('', StudentListCreateView.as_view(), name='student-list-create'),
    path('<int:pk>/',
         StudentRetrieveUpdateDeleteView.as_view(),
         name='student-detail'),
]
