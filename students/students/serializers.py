from rest_framework.serializers import ModelSerializer
from sample.student import Student



class StudentSerializer(ModelSerializer):
    class Meta:
        model = Student
        fields = '__all__'
