from django.shortcuts import render
from rest_framework import generics
from .serializers import UserSerializer,AppointmentsSerialzer
from rest_framework.permissions import IsAuthenticated, AllowAny
from .models import User, Appointment

class AppointmentListCreates(generics.ListCreateAPIView):
    serilizer_class = AppointmentsSerialzer
    permission_classes = [IsAuthenticated]

    def get_querryset(self):
        user = self.request.user
        return Appointment.objects.filter(patient = user)
    
    def preform_create(self, serializer):
        if serializer.is_valid():
            serializer.save(patient = self.request.user)
        else:
            print(serializer.errors)

class AppointmentDelete(generics.DestroyAPIView):
    serilizer_class = AppointmentsSerialzer
    permission_classes = [IsAuthenticated]

    def get_querryset(self):
        user = self.request.user
        return Appointment.objects.filter(patient = user)
    
class CreateUserView(generics.CreateAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer
    permission_classes = [AllowAny]