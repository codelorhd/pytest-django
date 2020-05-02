from rest_framework.generics import ListAPIView, CreateAPIView, DestroyAPIView, RetrieveAPIView
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from .serializers import StudentSerializer, ClassroomSerializer
from classroom.models import Student, ClassRoom


class StudentListAPIView(ListAPIView):
    serializer_class = StudentSerializer
    model = Student
    queryset = Student.objects.all()


class StudentCreateAPIView(CreateAPIView):
    serializer_class = StudentSerializer
    model = Student
    queryset = Student.objects.all()


class StudentDetailAPIView(RetrieveAPIView):
    serializer_class = StudentSerializer
    model = Student
    queryset = Student.objects.all()


class StudentDeleteAPIView(DestroyAPIView):
    serializer_class = StudentSerializer
    model = Student
    queryset = Student.objects.all()


class ClassRoomStudentCount(APIView):
    serializer_class = ClassroomSerializer
    model = ClassRoom
    queryset = ClassRoom.objects.all()

    def get(self, *args, **kwargs):
        capacity = self.kwargs.get('capacity')

        classroom_qs = ClassRoom.objects.filter(
            student_capacity__gte=capacity
        )
        serialized_data = ClassroomSerializer(classroom_qs, many=True)

        # take note of the serilizqation process (from model to dict)
        if serialized_data.is_valid:
            return Response(
                {
                    "classroom_data": serialized_data.data,
                    "number_classes": len(serialized_data.data)
                }, status=status.HTTP_200_OK)
        else:
            print(serialized_data.is_valid())
            return Response({"error": "Could not serialied data"})
