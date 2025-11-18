from rest_framework import generics
from .models import Student
from .models import models

class StudentListCreateView(generics.ListCreateAPIView):
    queryset = Student.objects.all()
    serializer_class = models


class StudentRetrieveUpdateDeleteView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Student.objects.all()
    serializer_class = models
